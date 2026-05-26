from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def bienvenida():
    return {"Bienvenida": "Bienvenido a la API de Inventario PV"}