# pyrefly: ignore [missing-import]
from fastapi import HTTPException
# pyrefly: ignore [missing-import]
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from app.service.encryptar import cifrar, descifrar

def _table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_passwords)

def recuperar_contraseñas():
    try:
        res = _table().select('*').execute()
        if res.data:
            for item in res.data:
                if item.get("password"):
                    item["password"] = descifrar(item["password"])
            return res.data
        else:
            raise HTTPException(status_code=404, detail="Contraseñas no encontradas")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar contraseñas: {str(e)}")

def agregar_contraseña(data: dict):
    try:
        if not data or not data.get("password"):
            raise HTTPException(status_code=400, detail="Datos incompletos o contraseña ausente")
        # Cifrar automáticamente desde el service
        data["password"] = cifrar(data["password"]).decode()
        data = jsonable_encoder(data)
        res = _table().insert(data).execute()
        item = res.data[0] if res.data else None
        # Descifrar para devolverlo en el JSON
        if item and item.get("password"):
            item["password"] = descifrar(item["password"])
        return {"items": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar la contraseña: {str(e)}")

def actualizar_contraseña(id_pass: str, data: dict):
    try:
        if not data:
            raise HTTPException(status_code=400, detail="Datos incompletos")
        # Si se incluye una contraseña, cifrarla
        if data.get("password"):
            data["password"] = cifrar(data["password"]).decode()
        data = jsonable_encoder(data)
        res = _table().update(data).eq("id_pass", id_pass).execute()
        item = res.data[0] if res.data else None
        # Descifrar para devolverlo en el JSON
        if item and item.get("password"):
            item["password"] = descifrar(item["password"])
        return {"items": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la contraseña: {str(e)}")

def eliminar_contraseña(id_pass: str):
    try:
        res = _table().delete().eq("id_pass", id_pass).execute()
        item = res.data[0] if res.data else None
        if item and item.get("password"):
            item["password"] = descifrar(item["password"])
        return {"items": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la contraseña: {str(e)}")

def buscar_contraseña(id_pass: str):
    try:
        res = _table().select("*").eq("id_pass", id_pass).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Contraseña no encontrada")
        item = res.data[0]
        if item.get("password"):
            item["password"] = descifrar(item["password"])
        return {"items": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar la contraseña: {str(e)}")
    