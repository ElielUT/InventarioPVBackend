from pydantic import BaseModel

class UtilizaModel(BaseModel):
    idutiliza: int
    idproc1: int
    idinvt2: int
    cantidad: int

class UtilizaRegistro(BaseModel):
    idproc1: int
    idinvt2: int
    cantidad: int

class RecuperarUtiliza(BaseModel):
    items: list[UtilizaModel]
    inventario: list[dict]

class RecuperarUnUtiliza(BaseModel):
    item: UtilizaModel