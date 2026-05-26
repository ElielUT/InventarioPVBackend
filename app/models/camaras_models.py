from pydantic import BaseModel

class CamarasModel(BaseModel):
    idprod1: int
    idcamara: int
    nombre: str
    direccionip: str
    ubicacion: str
    conexion: str

class RegistroCamara(BaseModel):
    idprod1: int
    nombre: str
    direccionip: str
    ubicacion: str
    conexion: str

class RecuperarCamaras(BaseModel):
    items: list[CamarasModel]

class RecuperarCamara(BaseModel):
    item: CamarasModel