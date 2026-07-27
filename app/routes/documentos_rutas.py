# pyrefly: ignore [missing-import]
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.service.documentos_service import subir_archivo, recuperar_archivos, recuperar_archivo

router = APIRouter(prefix="/documento", tags=["Documento"])

@router.post("/")
async def postDocumento(archivo: UploadFile = File(...)):
    return await subir_archivo(archivo)

@router.get("/")
def getDocumentos():
    return {"items": recuperar_archivos()}

@router.get("/{nombre_archivo}")
async def getDocumento(nombre_archivo: str):
    return await recuperar_archivo(nombre_archivo)