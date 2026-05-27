from datetime import date
from pydantic import BaseModel, Field

class ProcesoModel(BaseModel):
    idproc: int
    realizado: date
    idmant1: int

class ProcesoRegistro(BaseModel):
    realizado: date
    idmant1: int

class RecuperarProceso(BaseModel):
    items: list[ProcesoModel]

class RecuperarUnProceso(BaseModel):
    item: ProcesoModel
    