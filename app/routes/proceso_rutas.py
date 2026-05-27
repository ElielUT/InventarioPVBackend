# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.proceso_model import ProcesoRegistro, RecuperarProceso
from app.service.proceso_service import agregarProceso, recuperarProceso, actualizarProceso, eliminarProceso

router = APIRouter(prefix="/proceso", tags=["Proceso"])

@router.get("/", response_model=RecuperarProceso)
def getProceso():
    res = recuperarProceso()
    return {"items": res}

@router.post("/", response_model=ProcesoRegistro)
def postProceso(item: ProcesoRegistro):
    res = agregarProceso(item.model_dump())
    return res.get("items")

@router.put("/{idproc}", response_model=ProcesoRegistro)
def putProceso(idproc: int, item: ProcesoRegistro):
    res = actualizarProceso(idproc, item.model_dump())
    return res.get("items")

@router.delete("/{idproc}", response_model=ProcesoRegistro)
def deleteProceso(idproc: int):
    res = eliminarProceso(idproc)
    return res.get("items")