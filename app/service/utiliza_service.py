# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from app.service.inventario_service import buscarInventario
from app.service.proceso_service import buscarProceso


def _Table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_utiliza)

def agregarUtiliza(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        if buscarInventario(data["idinvt2"]) is None:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        if buscarProceso(data["idproc1"]) is None:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
        res = _Table().insert(data).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar proceso: {str(e)}")

def recuperarUtiliza():
    try:
        res = _Table().select('*').execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar proceso: {str(e)}")

def actualizarUtiliza(idproc: int, data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().update(data).eq('idproc', idproc).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar proceso: {str(e)}")

def eliminarUtiliza(idproc: int):
    try:
        res = _Table().delete().eq('idproc', idproc).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar proceso: {str(e)}")

def buscarUtiliza(idproc: int):
    try:
        res = _Table().select('*').eq('idproc', idproc).execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar proceso: {str(e)}")