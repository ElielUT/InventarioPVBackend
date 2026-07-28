from typing import Optional
# pyrefly: ignore [missing-import]
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.service.documentos_service import subir_archivo, recuperar_archivos, recuperar_archivo, eliminar_documento

router = APIRouter(prefix="/documento", tags=["Documento"])

@router.post("/")
async def postDocumento(archivo: UploadFile = File(...), categoria: Optional[str] = Form("Otros")):
    return await subir_archivo(archivo, categoria or "Otros")

@router.get("/")
def getDocumentos():
    return {"items": recuperar_archivos()}

@router.get("/{nombre_archivo}")
async def getDocumento(nombre_archivo: str):
    return await recuperar_archivo(nombre_archivo)

@router.delete("/{identificador}")
def deleteDocumento(identificador: str):
    return eliminar_documento(identificador)