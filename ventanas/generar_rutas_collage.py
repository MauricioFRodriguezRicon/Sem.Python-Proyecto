import os
import json
import csv
from PIL import Image,ImageTk,ImageDraw
# modulo que devuelve los directorios seleccionados en configuracion
def ruta_directorio():
   ruta_json=os.path.join(os.path.dirname(__file__),"json")
   ruta_json=os.path.join(ruta_json,"carpetas.json")
   with open(ruta_json,"r",encoding="UTF-8")as arch:
      arch.seek(0)
      dir=arch.read()
      imagen=json.loads(dir)
   return imagen
# modulo que devuelve  una lista de imagenes etiquetadas
def imagenes_csv():
   archivo = os.path.join(os.path.dirname(__file__), "csv", "imagenes.csv")  # rutacsv
   data=[]
   with open(archivo, "r") as arch:
      csv_reader = csv.reader(arch, delimiter=",")
      encabezado = next(csv_reader)   
      for fila in csv_reader:
         data.append(fila[0])
   return data
#modulo que devuelve la ruta de la imagen seleccionada para el collage
def ruta_imagen_celeccionada(imag_selec): 
      ruta_proyecto = os.path.abspath(os.path.dirname(__file__))  # tomo la ruta del proyecto
      ruta_imagen = os.path.join(ruta_proyecto, "imagenes",imag_selec)  # hago una ruta de la imagen seleccionada
      return ruta_imagen
# ajsuta imagen a una tamaño especifico
def ajusta_imagen( imagen,ancho,alto):
    imag_original=Image.open(imagen)
    resized_imagen=imag_original.resize((ancho,alto))
    return resized_imagen
    
#modulo que agregar el titulo del collage en una cordenada especifica
def agregar_titulo(window,collage,titulo): 
    draw=ImageDraw.Draw(collage)
    draw.text((15,480),titulo,fill="red")
    draw=ImageTk.PhotoImage(collage)
    window["-IMAGE-"].update(data=draw)

#modulo que guarda el collage completo
def guardar_collage(cop,titulo,directorio):
    
   if(os.path.isabs(directorio)):
      ruta = os.path.join(directorio)
   else:
      path = os.path.dirname(os.path.abspath(__file__))
      ruta = os.path.join(path,directorio)
   nombre=titulo+".PNG"
   ruta_collage=os.path.join(ruta,nombre) #Agrega el nombre a la direccion para guardarse
   cop.save(ruta_collage,format="PNG")