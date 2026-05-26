from fastapi import APIRouter
from app.models.inventario_model import InventarioModel,InventarioRegistro
from app.service.inventario_service import agregarInventario,recuperarInventario

router = APIRouter(prefix="/inventario", tags=["Inventario"])

@router.get("/", response_model=list[InventarioModel])
def obtenerInventario():
    return recuperarInventario()
    
@router.post("/", response_model=InventarioRegistro)
def postInventario(item: InventarioRegistro):
    res = agregarInventario(item.model_dump())
    return res.get("items")