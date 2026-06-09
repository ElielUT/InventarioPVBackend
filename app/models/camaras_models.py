from pydantic import BaseModel
from app.models.productos_model import ProductoModel

class CamarasModel(BaseModel):
    idprod2: int
    idcamara: int
    nombre: str
    direccioip: str
    ubicacion: str
    conexion: str

class RegistroCamara(BaseModel):
    idprod2: int
    nombre: str
    direccioip: str
    ubicacion: str
    conexion: str

class RecuperarCamaras(BaseModel):
    items: list[CamarasModel]
    productos: list[ProductoModel]

class RecuperarCamara(BaseModel):
    item: CamarasModel