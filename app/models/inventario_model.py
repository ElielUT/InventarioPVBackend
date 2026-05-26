from pydantic import BaseModel, Field, ConfigDict

class InventarioModel(BaseModel):
    idinvt: int
    producto: str 
    categoria: str
    cantidad: int
    medida: int | None = Field(None)
    unmed: str | None = Field(None, max_length=4)

class InventarioRegistro(BaseModel):
    producto: str 
    categoria: str
    cantidad: int
    medida: int | None = Field(None)
    unmed: str | None = Field(None, max_length=4)