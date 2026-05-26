# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config

from app.service.inventario_service import buscarInventario

def _Table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_productos)

def agregarProducto(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        inventario = buscarInventario(data["idinvt1"])
        if not inventario:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        data = jsonable_encoder(data)
        res = _Table().insert(data).execute()
        return {"items": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar el Producto: {e}")

def recuperarProducto():
    try:
        res = _Table().select("*").execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="No se encontro ningun producto")
        return res.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar el Producto: {e}")

def actualizarProducto(id:int, data:dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        data = jsonable_encoder(data)
        res = _Table().update(data).eq("idprod", id).execute()
        return {"items": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el Producto: {e}")

def eliminarProducto(id:int):
    try:
        res = _Table().delete().eq("idprod", id).execute()
        return {"items": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el Producto: {e}")
    
def buscarProducto(idprod: int):
    try:
        res = _Table().select("*").eq("idprod", idprod).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="No se encontro ningun producto")
        return res.data[0] 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar el Producto: {e}")