# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException
# pyrefly: ignore [missing-import]
from app.models.productos_model import ProductoModel,RegistroProducto, RecuperarProductos, RecuperarUnProducto
# pyrefly: ignore [missing-import]
from app.service.producto_service import agregarProducto,recuperarProducto, actualizarProducto, eliminarProducto

router = APIRouter(prefix="/producto", tags=["Producto"])

@router.get("/", response_model=RecuperarProductos)
def obtenerProductos():
    res = recuperarProducto()
    return {"items": res}
    
@router.post("/", response_model=RegistroProducto)
def postProducto(item: RegistroProducto):
    res = agregarProducto(item.model_dump())
    return res.get("items")

@router.put("/{idprod}", response_model=RegistroProducto)
def putProducto(idprod: int, item: RegistroProducto):
    res = actualizarProducto(idprod, item.model_dump())
    return res.get("items")

@router.delete("/{idprod}", response_model=RegistroProducto)
def deleteProducto(idprod: int):
    res = eliminarProducto(idprod)
    return res.get("items")