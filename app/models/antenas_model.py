from pydantic import BaseModel, Field, ConfigDict

class AntenaModel(BaseModel):
    idprod1: int
    idantena: int
    nombre: str
    direccionip: str
    usuario: str
    contrasena: str
    ubicacion: str
    puertoswitch: str

class RegistroAntena(BaseModel):
    idprod1: int
    nombre: str
    direccionip: str
    usuario: str
    contrasena: str
    ubicacion: str
    puertoswitch: str

class RecuperarAntenas(BaseModel):
    items: list[AntenaModel]

class RecuperarAntena(BaseModel):
    item: AntenaModel