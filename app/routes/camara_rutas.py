# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.camaras_models import RegistroCamara, RecuperarCamaras
from app.service.camara_sercice import agregarCamara,recuperarCamaras, actualizarCamara, eliminarCamara
from app.service.producto_service import buscarProductoCategoria

router = APIRouter(prefix="/camara", tags=["Camara"])

@router.get("/", response_model=RecuperarCamaras)
def obtenerCamaras():
    res = recuperarCamaras()
    return {"items": res,
            "productos": buscarProductoCategoria("Cámaras")}

@router.post("/", response_model=RegistroCamara)
def postCamara(item: RegistroCamara):
    res = agregarCamara(item.model_dump())
    return res

@router.put("/{idcamara}", response_model=RegistroCamara)
def putCamara(idcamara: int, item: RegistroCamara):
    res = actualizarCamara(idcamara, item.model_dump())
    return res

@router.delete("/{idcamara}", response_model=RegistroCamara)
def deleteCamara(idcamara: int):
    res = eliminarCamara(idcamara)
    return res