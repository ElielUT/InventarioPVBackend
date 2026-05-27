# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.camaras_models import RegistroCamara, RecuperarCamaras
from app.service.camara_sercice import agregarCamara,recuperarCamaras, actualizarCamara, eliminarCamara

router = APIRouter(prefix="/camara", tags=["Camara"])

@router.get("/", response_model=RecuperarCamaras)
def obtenerCamaras():
    res = recuperarCamaras()
    return {"items": res}

@router.post("/", response_model=RegistroCamara)
def postCamara(item: RegistroCamara):
    res = agregarCamara(item.model_dump())
    return res.get("items")

@router.put("/{idcamara}", response_model=RegistroCamara)
def putCamara(idcamara: int, item: RegistroCamara):
    res = actualizarCamara(idcamara, item.model_dump())
    return res.get("items")

@router.delete("/{idcamara}", response_model=RegistroCamara)
def deleteCamara(idcamara: int):
    res = eliminarCamara(idcamara)
    return res.get("items")