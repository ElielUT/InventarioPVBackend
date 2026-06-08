# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from app.models.passwords_model import PasswordsRegistro, PasswordsModel, RecuperarPasswords, RecuperarPasswordsUn
from app.service.passwords_service import (
    recuperar_contraseñas,
    agregar_contraseña,
    actualizar_contraseña,
    eliminar_contraseña,
    buscar_contraseña
)

router = APIRouter(prefix="/passwords", tags=["Passwords"])

@router.get("/", response_model=RecuperarPasswords)
def obtenerPasswords():
    res = recuperar_contraseñas()
    return {"items": res}

@router.post("/", response_model=PasswordsModel)
def postPassword(item: PasswordsRegistro):
    res = agregar_contraseña(item.model_dump())
    return res.get("items")

@router.put("/{id_pass}", response_model=PasswordsModel)
def putPassword(id_pass: str, item: PasswordsRegistro):
    res = actualizar_contraseña(id_pass, item.model_dump())
    return res.get("items")

@router.delete("/{id_pass}", response_model=PasswordsModel)
def deletePassword(id_pass: str):
    res = eliminar_contraseña(id_pass)
    return res.get("items")

@router.get("/{id_pass}", response_model=RecuperarPasswordsUn)
def getUnPassword(id_pass: str):
    res = buscar_contraseña(id_pass)
    return {"item": res.get("items")}
