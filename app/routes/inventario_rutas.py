# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.inventario_model import InventarioModel,InventarioRegistro, RecuperarInventario, RecuperarUnInventario
from app.service.inventario_service import agregarInventario,recuperarInventario, actualizarInventario, eliminarInventario, buscarInventario

router = APIRouter(prefix="/inventario", tags=["Inventario"])

@router.get("/", response_model=RecuperarInventario)
def obtenerInventario():
    res = recuperarInventario()
    return {"items": res}
    
@router.post("/", response_model=InventarioRegistro)
def postInventario(item: InventarioRegistro):
    res = agregarInventario(item.model_dump())
    return res.get("items")

@router.put("/{idinvt}", response_model=InventarioRegistro)
def putInventario(idinvt: int, item: InventarioRegistro):
    res = actualizarInventario(idinvt, item.model_dump())
    return res.get("items")

@router.delete("/{idinvt}", response_model=InventarioRegistro)
def deleteInventario(idinvt: int):
    res = eliminarInventario(idinvt)
    return res.get("items")

@router.get("/{idinvt}", response_model=RecuperarUnInventario)
def getUnInventario(idinvt: int):
    res = buscarInventario(idinvt)
    return res.get("items")