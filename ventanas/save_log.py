import os
import json
import csv
from datetime import datetime


def registro_log(user, evento,valores = "",textos = ""):
    ruta_json = os.path.join(os.path.dirname(__file__), "json")
    ruta_json = os.path.join(ruta_json, "perfiles.json")
    with open(ruta_json, encoding="utf-8") as arch:
        arch.seek(0)
        lista_usuarios = arch.read()
        lista_usuarios = json.loads(lista_usuarios)
        alias = lista_usuarios[user]["alias"]
    timestamp = datetime.timestamp(datetime.now())
    fecha_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

    ruta_log = os.path.join(os.path.dirname(__file__), "csv")
    ruta_log = os.path.join(ruta_log, "logs.csv")
    
    if(os.path.exists(ruta_log)):
        with open(ruta_log, "a") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([fecha_hora, alias, evento,valores,textos])
    else:
        with open(ruta_log,"w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Fecha y hora","Alias","Operacion","Valores","Textos"])
            writer.writerow([fecha_hora, alias, evento,valores,textos])