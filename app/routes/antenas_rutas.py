# pyrefly: ignore [missing-import]
from fastapi import APIRouter
# pyrefly: ignore [missing-import]
from app.models.antenas_model import RegistroAntena, RecuperarAntenas
# pyrefly: ignore [missing-import]
from app.service.antena_service import agregarAntena,recuperarAntenas, actualizarAntena, eliminarAntena
from app.service.producto_service import buscarProductoCategoria

router = APIRouter(prefix="/antena", tags=["Antena"])

@router.get("/", response_model=RecuperarAntenas)
def obtenerAntenas():
    res = recuperarAntenas()
    return {"items": res,
            "productos": buscarProductoCategoria("Antenas")}

@router.post("/", response_model=RegistroAntena)
def postAntena(item: RegistroAntena):
    res = agregarAntena(item.model_dump(by_alias=True))
    return res

@router.put("/{idantena}", response_model=RegistroAntena)
def putAntena(idantena: int, item: RegistroAntena):
    res = actualizarAntena(idantena, item.model_dump(by_alias=True))
    return res

@router.delete("/{idantena}", response_model=RegistroAntena)
def deleteAntena(idantena: int):
    res = eliminarAntena(idantena)
    return res
