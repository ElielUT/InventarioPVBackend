# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.utiliza_model import UtilizaRegistro, RecuperarUtiliza
from app.service.utiliza_service import agregarUtiliza,recuperarUtiliza, actualizarUtiliza, eliminarUtiliza

router = APIRouter(prefix="/utiliza", tags=["Utiliza"])

@router.get("/", response_model=RecuperarUtiliza)
def getUtiliza():
    res = recuperarUtiliza()
    return res

@router.post("/", response_model=UtilizaRegistro)
def postUtiliza(item: UtilizaRegistro):
    res = agregarUtiliza(item.model_dump())
    return res

@router.put("/{idutiliza}", response_model=UtilizaRegistro)
def putUtiliza(idutiliza: int, item: UtilizaRegistro):
    res = actualizarUtiliza(idutiliza, item.model_dump())
    return res

@router.delete("/{idutiliza}", response_model=UtilizaRegistro)
def deleteUtiliza(idutiliza: int):
    res = eliminarUtiliza(idutiliza)
    return res
