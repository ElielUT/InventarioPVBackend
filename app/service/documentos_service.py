import unicodedata
import re
# pyrefly: ignore [missing-import]
from fastapi import UploadFile, File, HTTPException, Response
from app.core.supabase_client import get_supabase
from app.core.config import config

def _Storage():
    return get_supabase().storage

def _Table():
    return get_supabase().schema(config.supabase_schema).table(config.supabase_documentos)

def sanitizar_nombre_archivo(nombre: str) -> str:
    nfkd = unicodedata.normalize('NFKD', nombre)
    sin_tildes = "".join([c for c in nfkd if not unicodedata.combining(c)])
    sin_espacios = sin_tildes.replace(" ", "_")
    nombre_limpio = re.sub(r'[^a-zA-Z0-9_.-]', '', sin_espacios)
    return nombre_limpio or "archivo"

async def subir_archivo(archivo: UploadFile = File(...), categoria: str = "Otros"):
    try:
        file_bytes = await archivo.read()
        file_name = sanitizar_nombre_archivo(archivo.filename or "archivo")        
        upload_response = _Storage().from_("documentos_soporte").upload(
            file = file_bytes,
            path = file_name,
            file_options = {
                "content-type": archivo.content_type,
                "x-upsert": "true"
            }
        )    
        public_url = _Storage().from_("documentos_soporte").get_public_url(file_name)
        cat_final = categoria.strip() if (categoria and categoria.strip()) else "Otros"
        datos = {
            "url": public_url,
            "nombre": file_name,
            "categoria": cat_final
        }
        res = _Table().insert(datos).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir el archivo: {str(e)}")

def recuperar_archivos():
    try:
        res = _Table().select("*").execute()
        if res.data and len(res.data) > 0:
            return res.data
        else:
            storage_res = _Storage().from_("documentos_soporte").list()
            return storage_res.data if storage_res.data else []
    except Exception:
        try:
            storage_res = _Storage().from_("documentos_soporte").list()
            return storage_res.data if storage_res.data else []
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al recuperar archivos: {str(e)}")

async def recuperar_archivo(nombre_archivo: str):
    try:
        file_bytes = _Storage().from_("documentos_soporte").download(nombre_archivo)
        return Response(
            content=file_bytes, 
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename="{nombre_archivo}"'}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar archivos: {str(e)}")

def eliminar_documento(identificador: str):
    try:
        nombre_archivo = None
        identificador_str = str(identificador).strip()

        if identificador_str.isdigit():
            res_db = _Table().select("*").eq("id_doc", int(identificador_str)).execute()
            if res_db.data and len(res_db.data) > 0:
                nombre_archivo = res_db.data[0].get("nombre")
                _Table().delete().eq("id_doc", int(identificador_str)).execute()
            else:
                _Table().delete().eq("nombre", identificador_str).execute()
                nombre_archivo = identificador_str
        else:
            nombre_archivo = identificador_str
            _Table().delete().eq("nombre", identificador_str).execute()

        if nombre_archivo:
            try:
                _Storage().from_("documentos_soporte").remove([nombre_archivo])
            except Exception as st_err:
                print(f"Error al eliminar de Storage: {st_err}")

        return {"message": "Documento eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el documento: {str(e)}")