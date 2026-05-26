# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config

def _Table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_inventario)

def agregarInventario(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().insert(data).execute()
        return {"items": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar el Inventario: {e}")

def recuperarInventario():
    try:
        res = _Table().select("*").execute()
        if res.data is None:
            raise HTTPException(status_code=404, detail="No se encontro inventario")
        return res.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar el Inventario: {e}")

#def actualizarInventario(id:int, data:dict):
    