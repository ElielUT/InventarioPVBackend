# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from app.service.producto_service import buscarProducto

def _Table():
    supabase = get_supabase()
    return supabase.schema(config.supabase_schema).table(config.supabase_antenas)

def recuperarAntenas():
    try:
        res = _Table().select('*').execute()
        if res.data:
            return res.data[0]
        else:
            raise HTTPException(status_code=404, detail="Antena no encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar antena: {str(e)}")

def agregarAntena(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        producto = buscarProducto(data["idprod1"])
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        data = jsonable_encoder(data)
        res = _Table().insert(data).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar antena: {str(e)}")

def actualizarAntena(idantena: int, data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().update(data).eq('idantena', idantena).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar antena: {str(e)}")

def eliminarAntena(idantena: int):
    try:
        res = _Table().delete().eq('idantena', idantena).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar antena: {str(e)}")