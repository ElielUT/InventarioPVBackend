# pyrefly: ignore [missing-import]
from fastapi import FastAPI, UploadFile, File, HTTPException, Response
from app.core.supabase_client import get_supabase
from app.core.config import config

def _Storage():
    return get_supabase().storage

def _Table():
    return get_supabase().schema(config.supabase_schema).table(config.supabase_documentos)

async def subir_archivo(archivo: UploadFile = File(...)):
    try:
        file_bytes = await archivo.read()
        file_name = archivo.filename.replace(" ", "_")        
        upload_response = _Storage().from_("documentos_soporte").upload(
            file = file_bytes,
            path = file_name,
            file_options = {
                "content-type": archivo.content_type,
                "x-upsert": "true"
            }
        )    
        public_url = _Storage().from_("documentos_soporte").get_public_url(file_name)
        datos = {
            "url": public_url,
            "nombre": file_name
        }
        res = _Table().insert(datos).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir el archivo: {str(e)}")

def recuperar_archivos():
    try:
        res = _Storage().from_("documentos_soporte").list()
        if res.data:
            return res.data
        else:
            return []
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