from pydantic import BaseModel, Field, ConfigDict
from app.models.productos_model import ProductoModel

class AntenaModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    idprod1: int
    idantena: int
    nombre: str
    direccionip: str
    usuario: str
    contrasena: str = Field(alias="contraseña")
    ubicacion: str
    puertoswitch: str

class RegistroAntena(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    idprod1: int
    nombre: str
    direccionip: str
    usuario: str
    contrasena: str = Field(alias="contraseña")
    ubicacion: str
    puertoswitch: str

class RecuperarAntenas(BaseModel):
    items: list[AntenaModel]
    productos: list[ProductoModel]

class RecuperarAntena(BaseModel):
    item: AntenaModel