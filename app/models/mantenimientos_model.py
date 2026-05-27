from pydantic import BaseModel, Field

class MantenimientosModel(BaseModel):
    idmant: int
    areas: str
    dia: int = Field(..., ge=1, le=31)
    mes: int = Field(..., ge=1, le=12)

class MantenimientosRegistro(BaseModel):
    areas: str
    dia: int = Field(..., ge=1, le=31)
    mes: int = Field(..., ge=1, le=12)

class RecuperarMantenimientos(BaseModel):
    items: list[MantenimientosModel]

class RecuperarUnMantenimiento(BaseModel):
    item: MantenimientosModel