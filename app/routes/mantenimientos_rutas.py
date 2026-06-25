# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.mantenimientos_model import MantenimientosRegistro, RecuperarMantenimientos
# pyrefly: ignore [missing-import]
from app.service.mantenimientos_service import agregarMantenimiento,recuperarMantenimientos, actualizarMantenimiento, eliminarMantenimiento

router = APIRouter(prefix="/mantenimientos", tags=["Mantenimientos"])

@router.get("/", response_model=RecuperarMantenimientos)
def getMantenimientos():
    res = recuperarMantenimientos()
    return {"items": res}

@router.post("/", response_model=MantenimientosRegistro)
def postMantenimientos(item: MantenimientosRegistro):
    res = agregarMantenimiento(item.model_dump())
    return res

@router.put("/{idmant}", response_model=MantenimientosRegistro)
def putMantenimientos(idmant: int, item: MantenimientosRegistro):
    res = actualizarMantenimiento(idmant, item.model_dump())
    return res

@router.delete("/{idmant}", response_model=MantenimientosRegistro)
def deleteMantenimientos(idmant: int):
    res = eliminarMantenimiento(idmant)
    return res
