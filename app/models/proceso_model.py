from datetime import date
from pydantic import BaseModel, Field
from app.models.mantenimientos_model import MantenimientosModel

class ProcesoModel(BaseModel):
    idproc: int
    realizado: date
    idmant1: int
    mantenimientos: MantenimientosModel | None = None

class ProcesoRegistro(BaseModel):
    realizado: date
    idmant1: int

class RecuperarProceso(BaseModel):
    items: list[ProcesoModel]
    mantenimientos: list[MantenimientosModel]

class RecuperarUnProceso(BaseModel):
    item: ProcesoModel
    