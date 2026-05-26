# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings, SettingsConfigDict
# pyrefly: ignore [missing-import]
from pydantic import Field

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        env_prefix= "",
    )
    
    supabase_url: str = Field(..., alias="SUPABASE_URL")
    supabase_key: str = Field(..., alias="SUPABASE_KEY")
    supabase_schema: str = Field(..., alias="SUPABASE_SCHEMA")
    supabase_inventario: str = Field(..., alias="SUPABASE_INVENTARIO")
    supabase_productos: str = Field(..., alias="SUPABASE_PRODUCTOS")
    supabase_antenas: str = Field(..., alias="SUPABASE_ANTENAS")
    supabase_camaras: str = Field(..., alias="SUPABASE_CAMARAS")
    supabase_mantenimientos: str = Field(..., alias="SUPABASE_MANTENIMIENTOS")
    supabase_proceso: str = Field(..., alias="SUPABASE_PROCESO")
    supabase_utiliza: str = Field(..., alias="SUPABASE_UTILIZA")

    encrypto_key: str = Field(..., alias="ENCRYPTION_KEY")

config = Config()