# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config

from app.service.inventario_service import buscarInventario, actualizarInventario

def _Table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_productos)

def agregarProducto(data: dict):
    try:
        if not data:
            raise HTTPException(status_code=404, detail="Datos incompletos")
        inventario = buscarInventario(data["idinvt1"])
        inventario_item = inventario.get("items") if inventario else None
        if not inventario_item:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        data = jsonable_encoder(data)
        res = _Table().insert(data).execute()
        
        # Incrementar en 1 la cantidad del inventario correspondiente
        if res.data:
            current_qty = inventario_item.get("cantidad", 0)
            actualizarInventario(data["idinvt1"], {"cantidad": current_qty + 1})
            
        return {"items": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar el Producto: {e}")

def recuperarProducto(idinvt1: int):
    try:
        res = _Table().select("*").eq("idinvt1", idinvt1).execute()
        inventario = buscarInventario(idinvt1)
        inventario_item = inventario.get("items") if inventario else None
        producto_nombre = inventario_item.get("producto") if inventario_item else "Desconocido"
        
        return {
            "items": res.data if res.data else [],
            "producto": producto_nombre,
            "idinvt": idinvt1
        }
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
        # Obtener el producto antes de eliminarlo para saber el idinvt1
        producto = buscarProducto(id)
        idinvt1 = producto.get("idinvt1") if producto else None
        
        res = _Table().delete().eq("idprod", id).execute()
        
        # Si se eliminó correctamente y tenemos el idinvt1, decrementar la cantidad del inventario
        if res.data and idinvt1:
            inventario = buscarInventario(idinvt1)
            inventario_item = inventario.get("items") if inventario else None
            if inventario_item:
                current_qty = inventario_item.get("cantidad", 0)
                actualizarInventario(idinvt1, {"cantidad": max(0, current_qty - 1)})
                
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