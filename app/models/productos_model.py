from pydantic import BaseModel, Field, ConfigDict

class ProductoModel(BaseModel):
    idprod:int
    idinvt1: int
    estado: str
    marca:str | None = Field(None)
    modelo: str | None = Field(None)
    noserie: str | None = Field(None)
    cvlicencia: str | None = Field(None)

class RegistroProducto(BaseModel):
    idinvt1: int
    estado: str
    marca:str | None = Field(None)
    modelo: str | None = Field(None)
    noserie: str | None = Field(None)
    cvlicencia: str | None = Field(None)

class RecuperarProductos(BaseModel):
    items: list[ProductoModel]

class RecuperarUnProducto(BaseModel):
    item: ProductoModel
