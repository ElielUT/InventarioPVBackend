# pyrefly: ignore [missing-import]
from fastapi import Request #Entrega URL
# pyrefly: ignore [missing-import]
from fastapi.exceptions import RequestValidationError #Entrega mensaje de error
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse #Preparar la respuesta

MENSAJES_ERROR = {
    # --- INVENTARIO ---
    "postInventario": {
        "producto": {
            "missing": "El nombre del producto es requerido",
            "string_too_long": "El nombre del producto no debe exceder los 100 caracteres"
        },
        "categoria": {
            "missing": "La categoría es requerida",
            "string_too_long": "La categoría no debe exceder los 50 caracteres"
        },
        "cantidad": {
            "missing": "La cantidad es requerida",
            "int_parsing": "La cantidad debe ser un número entero",
            "greater_than_equal": "La cantidad no puede ser negativa"
        },
        "unmed": {
            "string_too_long": "La unidad de medida no debe exceder los 4 caracteres"
        },
        "subcategoria": {
            "bool_parsing": "El campo subcategoría debe ser verdadero o falso"
        }
    },
    "putInventario": {
        "producto": {
            "missing": "El nombre del producto es requerido",
            "string_too_long": "El nombre del producto no debe exceder los 100 caracteres"
        },
        "categoria": {
            "missing": "La categoría es requerida",
            "string_too_long": "La categoría no debe exceder los 50 caracteres"
        },
        "cantidad": {
            "missing": "La cantidad es requerida",
            "int_parsing": "La cantidad debe ser un número entero",
            "greater_than_equal": "La cantidad no puede ser negativa"
        },
        "unmed": {
            "string_too_long": "La unidad de medida no debe exceder los 4 caracteres"
        }
    },

    # --- PRODUCTOS ---
    "postProducto": {
        "idinvt1": {
            "missing": "El ID del inventario es requerido",
            "int_parsing": "El ID del inventario debe ser un número entero"
        },
        "estado": {
            "missing": "El estado del producto es requerido",
            "string_too_long": "El estado no debe exceder los 30 caracteres"
        }
    },
    "putProducto": {
        "idinvt1": {
            "missing": "El ID del inventario es requerido",
            "int_parsing": "El ID del inventario debe ser un número entero"
        },
        "estado": {
            "missing": "El estado del producto es requerido",
            "string_too_long": "El estado no debe exceder los 30 caracteres"
        }
    },

    # --- CÁMARAS ---
    "postCamara": {
        "idprod2": {
            "missing": "El ID del producto es requerido",
            "int_parsing": "El ID del producto debe ser un número entero"
        },
        "nombre": {
            "missing": "El nombre de la cámara es requerido"
        },
        "direccioip": {
            "missing": "La dirección IP es requerida"
        },
        "ubicacion": {
            "missing": "La ubicación es requerida"
        },
        "conexion": {
            "missing": "El tipo de conexión es requerido"
        }
    },
    "putCamara": {
        "idprod2": {
            "missing": "El ID del producto es requerido",
            "int_parsing": "El ID del producto debe ser un número entero"
        },
        "nombre": {
            "missing": "El nombre de la cámara es requerido"
        },
        "direccioip": {
            "missing": "La dirección IP es requerida"
        },
        "ubicacion": {
            "missing": "La ubicación es requerida"
        },
        "conexion": {
            "missing": "El tipo de conexión es requerido"
        }
    },

    # --- ANTENAS ---
    "postAntena": {
        "idprod1": {
            "missing": "El ID del producto es requerido",
            "int_parsing": "El ID del producto debe ser un número entero"
        },
        "nombre": {
            "missing": "El nombre de la antena es requerido"
        },
        "direccionip": {
            "missing": "La dirección IP es requerida"
        },
        "usuario": {
            "missing": "El usuario es requerido"
        },
        "contraseña": {
            "missing": "La contraseña es requerida"
        },
        "ubicacion": {
            "missing": "La ubicación es requerida"
        },
        "puertoswitch": {
            "missing": "El puerto del switch es requerido"
        }
    },
    "putAntena": {
        "idprod1": {
            "missing": "El ID del producto es requerido",
            "int_parsing": "El ID del producto debe ser un número entero"
        },
        "nombre": {
            "missing": "El nombre de la antena es requerido"
        },
        "direccionip": {
            "missing": "La dirección IP es requerida"
        },
        "usuario": {
            "missing": "El usuario es requerido"
        },
        "contraseña": {
            "missing": "La contraseña es requerida"
        },
        "ubicacion": {
            "missing": "La ubicación es requerida"
        },
        "puertoswitch": {
            "missing": "El puerto del switch es requerido"
        }
    },

    # --- MANTENIMIENTOS ---
    "postMantenimientos": {
        "areas": {
            "missing": "El área es requerida"
        },
        "dia": {
            "missing": "El día es requerido",
            "int_parsing": "El día debe ser un número entero",
            "greater_than_equal": "El día debe ser mayor o igual a 1",
            "less_than_equal": "El día no puede exceder 31"
        },
        "mes": {
            "missing": "El mes es requerido",
            "int_parsing": "El mes debe ser un número entero",
            "greater_than_equal": "El mes debe ser mayor o igual a 1",
            "less_than_equal": "El mes no puede exceder 12"
        }
    },
    "putMantenimientos": {
        "areas": {
            "missing": "El área es requerida"
        },
        "dia": {
            "missing": "El día es requerido",
            "int_parsing": "El día debe ser un número entero",
            "greater_than_equal": "El día debe ser mayor o igual a 1",
            "less_than_equal": "El día no puede exceder 31"
        },
        "mes": {
            "missing": "El mes es requerido",
            "int_parsing": "El mes debe ser un número entero",
            "greater_than_equal": "El mes debe ser mayor o igual a 1",
            "less_than_equal": "El mes no puede exceder 12"
        }
    },

    # --- PROCESO (REALIZADOS) ---
    "postProceso": {
        "realizado": {
            "missing": "La fecha de realización es requerida",
            "date_from_datetime_parsing": "El formato de fecha es inválido (use YYYY-MM-DD)"
        },
        "idmant1": {
            "missing": "El ID del mantenimiento es requerido",
            "int_parsing": "El ID del mantenimiento debe ser un número entero"
        }
    },
    "putProceso": {
        "realizado": {
            "missing": "La fecha de realización es requerida",
            "date_from_datetime_parsing": "El formato de fecha es inválido (use YYYY-MM-DD)"
        },
        "idmant1": {
            "missing": "El ID del mantenimiento es requerido",
            "int_parsing": "El ID del mantenimiento debe ser un número entero"
        }
    },

    # --- CONTRASEÑAS ---
    "postPassword": {
        "password": {
            "missing": "La contraseña es requerida"
        },
        "nombre": {
            "missing": "El nombre es requerido"
        },
        "categoria": {
            "missing": "La categoría es requerida"
        },
        "usuario": {
            "missing": "El usuario es requerido"
        }
    },
    "putPassword": {
        "password": {
            "missing": "La contraseña es requerida"
        },
        "nombre": {
            "missing": "El nombre es requerido"
        },
        "categoria": {
            "missing": "La categoría es requerida"
        },
        "usuario": {
            "missing": "El usuario es requerido"
        }
    },

    # --- UTILIZA (INSUMOS DE MANTENIMIENTO) ---
    "postUtiliza": {
        "idproc1": {
            "missing": "El ID del proceso es requerido",
            "int_parsing": "El ID del proceso debe ser un número entero"
        },
        "idinvt2": {
            "missing": "El producto del inventario es requerido",
            "int_parsing": "El ID del inventario debe ser un número entero"
        },
        "cantidad": {
            "missing": "La cantidad es requerida",
            "int_parsing": "La cantidad debe ser un número entero",
            "greater_than_equal": "La cantidad no puede ser negativa"
        }
    },
    "putUtiliza": {
        "idproc1": {
            "missing": "El ID del proceso es requerido",
            "int_parsing": "El ID del proceso debe ser un número entero"
        },
        "idinvt2": {
            "missing": "El producto del inventario es requerido",
            "int_parsing": "El ID del inventario debe ser un número entero"
        },
        "cantidad": {
            "missing": "La cantidad es requerida",
            "int_parsing": "La cantidad debe ser un número entero",
            "greater_than_equal": "La cantidad no puede ser negativa"
        }
    }
}

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors=[] #SE prepara una lista para almacenar todos los errores
    ruta_obj = request.scope.get("route") #Entrega la ruta completa
    ruta_name = getattr(ruta_obj, "name", "") #Entrega solo el atributo name y si no lo encuentra regresa None
    print(f"Ruta: {ruta_name}")
    print(f"Errores: {exc.errors()}")
    
    for error in exc.errors():
        parametro = error["loc"][-1] 
        tipo = error["type"]
        
        ruta_dic = MENSAJES_ERROR.get(ruta_name, {})
        parametro_dicc = ruta_dic.get(parametro, {})
        
        # Fallbacks: 
        # 1. Custom message for specific error type
        # 2. Generic default for that parameter if we have the param key but not the type key (not implemented here per se, but useful concept)
        # 3. Generic "Error en parámetro X"
        
        mensaje = parametro_dicc.get(tipo, f"Error en el parámetro '{parametro}': {tipo}")
        
        # If we didn't find a custom message in the map, we use the default Pydantic msg or our fallback above
        # The user seems to want custom messages.
        
        errors.append({
            "parametro": parametro,
            "mensaje": mensaje,
            "tipo_error": tipo
        })

    return JSONResponse(
        status_code=422,
        content={
            "detalles": errors
        }
    )