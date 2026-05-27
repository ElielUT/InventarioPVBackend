# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from app.service.mantenimientos_service import buscarMantenimiento


def _Table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_procesos)

def agregarProceso(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        if buscarMantenimiento(data["idmant1"]) is None:
            raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
        res = _Table().insert(data).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar proceso: {str(e)}")

def recuperarProceso():
    try:
        res = _Table().select('*').execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar proceso: {str(e)}")

def actualizarProceso(idproc: int, data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().update(data).eq('idproc', idproc).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar proceso: {str(e)}")

def eliminarProceso(idproc: int):
    try:
        res = _Table().delete().eq('idproc', idproc).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar proceso: {str(e)}")

def buscarProceso(idproc: int):
    try:
        res = _Table().select('*').eq('idproc', idproc).execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Proceso no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar proceso: {str(e)}")