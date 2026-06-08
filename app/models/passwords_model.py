from pydantic import BaseModel
from pydantic import Field

class PasswordsModel(BaseModel):
    id_pass: str = Field(None)
    password: str = Field(None)
    nombre: str = Field(None)
    categoria: str = Field(None)
    
class PasswordsRegistro(BaseModel):
    password: str = Field(None)
    nombre: str = Field(None)
    categoria: str = Field(None)

class RecuperarPasswords(BaseModel):
    items: list[PasswordsModel]

class RecuperarPasswordsUn(BaseModel):
    item: PasswordsModel