# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from app.service.inventario_service import buscarInventario, recuperarInventarioNomID, actualizarInventario
from app.service.proceso_service import buscarProceso


def _Table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_utiliza)

def agregarUtiliza(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        inv_res = buscarInventario(data["idinvt2"])
        if not inv_res or inv_res.get("items") is None:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        if buscarProceso(data["idproc1"]) is None:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
        res = _Table().insert(data).execute()
        inv_item = inv_res["items"]
        inv = actualizarInventario(data["idinvt2"], {"cantidad": inv_item["cantidad"] - data["cantidad"]})
        return {"utiliza": res.data[0], "inventario": inv}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar proceso: {str(e)}")

def recuperarUtiliza():
    try:
        res = _Table().select('*').execute()
        inv = recuperarInventarioNomID()
        return {"items": res.data, "inventario": inv}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar proceso: {str(e)}")

def actualizarUtiliza(idproc: int, data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        busqueda = buscarUtiliza(idproc)
        if busqueda is None:
            raise HTTPException(status_code=404, detail="No se encontro el proceso")
        res = _Table().update(data).eq('idutiliza', idproc).execute()
        inv_res = buscarInventario(data["idinvt2"])
        if not inv_res or inv_res.get("items") is None:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        inv_item = inv_res["items"]
        if data["cantidad"] > busqueda["cantidad"]:
            inv = actualizarInventario(data["idinvt2"], {"cantidad": inv_item["cantidad"] - (data["cantidad"] - busqueda["cantidad"])})
        elif data["cantidad"] < busqueda["cantidad"]:
            inv = actualizarInventario(data["idinvt2"], {"cantidad": inv_item["cantidad"] + (busqueda["cantidad"] - data["cantidad"])})
        else:
            inv = inv_res
        return {"utiliza": res.data[0], "inventario": inv}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar proceso: {str(e)}")

def eliminarUtiliza(idproc: int):
    try:
        res = _Table().delete().eq('idutiliza', idproc).execute()
        inv_res = buscarInventario(res.data[0]["idinvt2"])
        if not inv_res or inv_res.get("items") is None:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        inv_item = inv_res["items"]
        inv = actualizarInventario(res.data[0]["idinvt2"], {"cantidad": inv_item["cantidad"] + res.data[0]["cantidad"]})
        return {"utiliza": res.data[0], "inventario": inv}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar proceso: {str(e)}")

def buscarUtiliza(idproc: int):
    try:
        res = _Table().select('*').eq('idutiliza', idproc).execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar proceso: {str(e)}")