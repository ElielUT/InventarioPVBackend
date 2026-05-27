# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config

def _Table():
    supabase = get_supabase()
    return supabase.schema(config.supabase_schema).table(config.supabase_mantenimientos)

def recuperarMantenimientos():
    try:
        res = _Table().select('*').execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar mantenimiento: {str(e)}")

def agregarMantenimiento(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().insert(data).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar mantenimiento: {str(e)}")

def actualizarMantenimiento(idmant: int, data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().update(data).eq('idmant', idmant).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar mantenimiento: {str(e)}")

def eliminarMantenimiento(idmant: int):
    try:
        res = _Table().delete().eq('idmant', idmant).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar mantenimiento: {str(e)}")

def buscarMantenimiento(idmant: int):
    try:
        res = _Table().select('*').eq('idmant', idmant).execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar mantenimiento: {str(e)}")
    