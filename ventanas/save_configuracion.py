import os
import json


def save_configuracion(value):
    # se guarda las direcciones de las carpetas selecionadas en load_configuraciones
    ruta_json = os.path.join(os.path.dirname(__file__), "json")
    ruta_json = os.path.join(ruta_json, "carpetas.json")

    nuevo = value

    try:
        arch = open(ruta_json, "w", encoding="utf-8")
    except FileNotFoundError:
        arch = open(ruta_json, "xw", encoding="utf-8")
    finally:
        arch.write(json.dumps(nuevo, indent=4))
