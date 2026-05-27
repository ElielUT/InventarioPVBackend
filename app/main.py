# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
from app.routes import rutas, inventario_rutas, productos_rutas, camara_rutas, antenas_rutas, mantenimientos_rutas, proceso_rutas, utiliza_rutas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rutas.router)
app.include_router(inventario_rutas.router)
app.include_router(productos_rutas.router)
app.include_router(camara_rutas.router)
app.include_router(antenas_rutas.router)
app.include_router(mantenimientos_rutas.router)
app.include_router(proceso_rutas.router)
app.include_router(utiliza_rutas.router)

#python -m venv venv
# .\venv\Scripts\activate
# uvicorn app.main:app --reload
#deactivate
#pip freeze > requirements.txt


# Crear entorno virtual
# python -m venv venv

# Activar entorno virtual
# Windows: venv\Scripts\activate

# Salir del entorno virtual
# deactivate

# Instalar el framework y servidor
# pip install fastApi uvicorn

# Crear archivo con todas las instalaciones
# pip freeze > requirements.txt

# Instalar lo que está en requirements.txt
# pip install -r requirements.txt

# Ejecutar programa
# uvicorn app.main:app --reload