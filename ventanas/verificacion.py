import os
import json


def verificar():
    """Se  ubica el path de los json"""
    path,terminacion = os.path.split(os.path.dirname(os.path.abspath(__file__)))
    path_carpetas = os.path.join(path,"ventanas/json/carpetas.json")

    """Si el archivo json con los path no existe se crea uno con los path por defecto"""
    if not(os.path.exists(path_carpetas)):
        with open(path_carpetas,"x") as carpetas:
            direc = {'imagen' :  "imagenes",
                     'collage':  "Collage",
                     'meme':  "memes"
                    }
            json.dump(direc,carpetas,indent=4)