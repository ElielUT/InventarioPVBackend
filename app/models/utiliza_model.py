from datetime import date
from pydantic import BaseModel

class UtilizaModel(BaseModel):
    idproc1: int
    idinvt2: int
    cantidad: int

class UtilizaRegistro(BaseModel):
    idproc1: int
    idinvt2: int
    cantidad: int

class RecuperarUtiliza(BaseModel):
    items: list[UtilizaModel]

class RecuperarUnUtiliza(BaseModel):
    item: UtilizaModel