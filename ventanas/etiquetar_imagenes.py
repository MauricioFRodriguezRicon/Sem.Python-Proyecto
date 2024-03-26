import PySimpleGUI as sg
import ventanas.constantes as c
import json
import os
from PIL import Image
import csv
from datetime import datetime
import ventanas.save_log as log
import ventanas.inicio as inicio

def leer_csv():
    """
    funcion que me devuelve los datos de un csv en una lista
    """
    archivo = os.path.join(os.path.dirname(__file__), "csv", "imagenes.csv")  # rutacsv

    with open(archivo, "r") as arch:
        csv_reader = csv.reader(arch, delimiter=",")
        data = []
        encabezado = next(csv_reader)
        for fila in csv_reader:
            #fila[5] = json.loads(fila[5])
            data.append(fila)
    return data


def cargar_csv():
    """
    tomo los datos de las fotos y los guardo en el csv cuando el csv no existe
    """
    archivos = os.path.join(os.path.dirname(__file__), "imagenes")
    archivos_imagenes = [
        f for f in os.listdir(archivos) if os.path.isfile(os.path.join(archivos, f))and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    archivo = os.path.join(os.path.dirname(__file__), "csv", "imagenes.csv")  # rutacsv

    datos_imagenes = []
    for el in range(len(archivos_imagenes)):
        # datos de la imagen
        ruta_imagen = archivos_imagenes[el]
        texto_descriptivo = " "
        im = Image.open(os.path.join(archivos, ruta_imagen))
        resolucion = im.size
        tamaño = round(os.path.getsize(os.path.join(archivos, ruta_imagen)) / 1024)
        tipo = im.format
        lista_tags = " "
        ult_perfil_actualizo = " "
        fecha_ult_actualizacion = " "
        datos_imagenes.append(
            [
                ruta_imagen,
                texto_descriptivo,
                resolucion,
                tamaño,
                tipo,
                lista_tags,
                ult_perfil_actualizo,
                fecha_ult_actualizacion,
            ]
        )

    if not os.path.exists(archivo):  # si el archivo no existe lo creo
        with open(archivo, "w", newline="") as arch:
            writer = csv.writer(arch)
            writer.writerow(
                [
                    "ruta_relativa",
                    "texto descriptivo",
                    "resolucion",
                    "tamanio",
                    "tipo",
                    "lista de tags",
                    "ultimo perfil que actualizo",
                    "ultima aztualizacion",
                ]
            )
            for elem in datos_imagenes:
                writer.writerow(elem)


def encontrar_en_lista(lista, nombre):
    """
    funcion que busca en una lista de listas si la primer pos de cada lista es igual al nombre pasado por parametro
    """
    datos = []
    for ele in range(len(lista)):
        if lista[ele][0] == nombre:
            pos = ele
            datos.append(pos)
            datos.append(lista[ele])
    return datos


def ventana_etiquetas(user,pos):
    cargar_csv()  # poongo los datos de las fotos en un csv
    data = leer_csv()  # me guardo los datos del csv en una lista

    archivos = os.path.join(os.path.dirname(__file__), "imagenes")
    archivos_imagenes = [
        f for f in os.listdir(archivos) if os.path.isfile(os.path.join(archivos, f))
    ]

    # creo la ventana dentro de una funcion para que pueda ser llamada desde la ventana de inicio
    layout_1 = [
        [
            sg.Listbox(
                values=archivos_imagenes,
                size=(30, 6),
                key="-LISTA-",
                enable_events=True,
                sbar_background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Tag",
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            )
        ],
        [
            sg.Input(key="-TAG-"),
            sg.Button(
                "Agregar",
                key="-AGREGAR-TAG-",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
            ),
        ],
        [
            sg.Text(
                "Texto descriptivo",
                text_color=c.COLOR_TEXTO,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Input(key="-TEXTO-", enable_events=True),
            sg.Button(
                "Agregar",
                key="-AGREGAR-TEXTO-",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
            ),
        ],
    ]

    layout_2 = [
        [
            sg.Text(
                "Imagen seleccionada",
                font=(12),
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Frame(
                " ",
                [
                    [
                        sg.Image(
                            key="-IMAGE-",
                            size=(200, 200),
                            background_color=c.COLOR_FONDO,
                        )
                    ]
                ],
                border_width=1,
                relief="solid",
                background_color=c.COLOR_FONDO,
            )
        ],
        [sg.Input(key="-IMG-", enable_events=True, size=(30))],
        [
            sg.Text("nombre:", key="-NOMBRE-", background_color=c.COLOR_FONDO),
            sg.Text("KB", key="-PESO-", background_color=c.COLOR_FONDO),
            sg.Text("res:", key="-DIMENSION-", background_color=c.COLOR_FONDO),
        ],
        [
            sg.DropDown(
                values="",
                enable_events=True,
                key="-ETIQUETAS-",
                size=(10, 6),
                button_background_color=c.COLOR_FONDO,
                button_arrow_color=c.COLOR_FONDO,
            ),
            sg.Button("X", key="-ELIMINAR-", button_color=c.COLOR_FONDO),
        ],
        [sg.Text(key="-TEXTO-DESCRIPTIVO-", background_color=c.COLOR_FONDO)],
        [
            sg.Button(
                "Guardar",
                key="-GUARDAR-",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=(" ", 12),
                pad=(76, 50),
            )
        ],
    ]

    layout_3 = [
        [
            sg.Column(
                [
                    [
                        sg.Button(
                            "< Volver",
                            key="-VOLVER-",
                            font=(" ", 12),
                            button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                        )
                    ]
                ],
                background_color=c.COLOR_FONDO,
                element_justification="right",
                justification="right",
            )
        ],
    ]

    # creo 3 layout para poder separar en la ventana

    # inserto esos layout en columnas para facilitar su manejo en la ventana
    columna_1 = sg.Column(layout_1, background_color=c.COLOR_FONDO, pad=(150, 80))
    columna_2 = sg.Column(layout_2, background_color=c.COLOR_FONDO)
    columna_3 = sg.Column(layout_3, background_color=c.COLOR_FONDO, expand_x=True)
    columnas = sg.Column(
        [[columna_3], [columna_1, columna_2]],
        background_color=c.COLOR_FONDO,
        expand_x=True,
        expand_y=True,
    )
    layout = [[[columnas]]]
    # creamos el objeto ventana
    window = sg.Window(
        "Etiquetar imagenes",
        layout,
        background_color=c.COLOR_FONDO,
        size=(1100, 700),
        resizable=False,
    )

    def crear_botones():
        """
        crea los botones para eliminar etiquetas
        """
        archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
        nombre = archivo_seleccionado[
            0
        ]  # con el nombre de la imagen lo bisco en la lista de datos del csv
        datos_img = encontrar_en_lista(
            data, nombre
        )  # una vez que lo encuentra me devuelve una lista con el primer valor la posicion donde lo encontro y la informacion de esa posicion
        lista_etiquetas = datos_img[1][5].split(',')
        return lista_etiquetas

    # un loop infinito para procesar los eventos de la ventana
    while True:
        event, values = window.read()

        if event == "OK" or event == sg.WIN_CLOSED:
            break
        elif event == "-VOLVER-":
            window.close()
            inicio.run()
            return True
        if event == "-LISTA-":
            archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
            img = archivo_seleccionado[0]
            ruta_proyecto = os.path.abspath(
                os.path.dirname(__file__)
            )  # tomo la ruta del proyecto
            ruta_imagen = os.path.join(ruta_proyecto, "imagenes", img)  # hago una ruta
            window["-IMAGE-"].update(
                filename=ruta_imagen,subsample=4,size = (200,200)
            )  # actualizo para que se vea la imagen
            var = os.path.relpath(ruta_imagen, ruta_proyecto)
            var2 = os.path.join("ventanas", var)
            window["-IMG-"].update(var2)
            window["-NOMBRE-"].update(f"| nombre:{img} |")
            window["-PESO-"].update(f"{round(os.path.getsize(ruta_imagen)/1024)} KB |")
            imagen = Image.open(ruta_imagen)
            window["-DIMENSION-"].update(f"res: {imagen.size} |")
            window["-ETIQUETAS-"].update(values=crear_botones())
            archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
            nombre = archivo_seleccionado[
                0
            ]  # con el nombre de la imagen lo bisco en la lista de datos del csv
            datos_img = encontrar_en_lista(
                data, nombre
            )  # una vez que lo encuentra me devuelve una lista con el primer valor la posicion donde lo encontro y la informacion de esa posicion
            texto = datos_img[1][1]
            window["-TEXTO-DESCRIPTIVO-"].update(f"texto descriptivo: {texto}")

        if event == "-ELIMINAR-":
            eliminado = values["-ETIQUETAS-"]  # tomo el elemento a eliminar
            archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
            nombre = archivo_seleccionado[0]
            datos_img = encontrar_en_lista(data, nombre)  # lo busco
            tags2 = datos_img[1][5].split(',')
            tags2.remove(eliminado)  # lo elimino
            texto = ','.join(tags2)
            datos_img[1][5] = texto

        if event == "-AGREGAR-TAG-":  # si se recibe el evento de agregar tag
            archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
            nombre = archivo_seleccionado[
                0
            ]  # con el nombre de la imagen lo bisco en la lista de datos del csv
            datos_img = encontrar_en_lista(
                data, nombre
            )  # una vez que lo encuentra me devuelve una lista con el primer valor la posicion donde lo encontro y la informacion de esa posicion 
            tags2 = datos_img[1][5].split(',')
            if(tags2[0]!=' '):
                tags2.append(values['-TAG-'])
                texto = ','.join(tags2)
            else:
                texto = values['-TAG-']
            datos_img[1][5] = texto # en la posicion 1 va a estar la informacion, ahi modifico el tag
            data[datos_img[0]] = datos_img[
                1
            ]  # en la posicion 0 va a estar la posicion donde se encontro la informacion en la lista de datos del csv

        if event == "-AGREGAR-TEXTO-":
            archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
            nombre = archivo_seleccionado[
                0
            ]  # con el nombre de la imagen lo bisco en la lista de datos del csv
            datos_img = encontrar_en_lista(
                data, nombre
            )  # una vez que lo encuentra me devuelve una lista con el primer valor la posicion donde lo encontro y la informacion de esa posicion
            datos_img[1][1] = values[
                "-TEXTO-"
            ]  # en la posicion 1 va a estar la informacion, ahi modifico el texto descriptivo
            data[datos_img[0]] = datos_img[
                1
            ]  # en la posicion 0 va a estar la posicion donde se encontro la informacion en la lista de datos del csv

        if event == "-GUARDAR-":
            archivo = os.path.join(
                os.path.dirname(__file__), "csv", "imagenes.csv"
            )  # rutacsv

            timestime = datetime.timestamp(datetime.now())
            

            archivo_seleccionado = values["-LISTA-"]  # tomo la imagen seleccionada
            nombre = archivo_seleccionado[
                0
            ]  # con el nombre de la imagen lo bisco en la lista de datos del csv
            datos_img = encontrar_en_lista(
                data, nombre
            )  # una vez que lo encuentra me devuelve una lista con el primer valor la posicion donde lo encontro y la informacion de esa posicion
            datos_img[1][7] = int(timestime)  # en la posicion 1 va a estar la informacion, ahi modifico el texto descriptivo
            ruta_json = os.path.join(os.path.dirname(__file__), "json")
            ruta_json = os.path.join(ruta_json, "perfiles.json")
            """Se bajan los datos del json para poder trabajar"""
            with open(ruta_json, encoding="utf-8") as arch:
                arch.seek(0)
                lista_usuarios = arch.read()
                lista_usuarios = json.loads(lista_usuarios)
                cual = lista_usuarios[pos]['nombre']
            datos_img[1][6] = cual
            if(datos_img[1][7] != []):
                ope = "Modificacion imagen Clasificada"
            else:
                ope ="Nueva imagen Clasificada"
            log.registro_log(user,ope)
            data[datos_img[0]] = datos_img[
                1
            ]  # en la posicion 0 va a estar la posicion donde se encontro la informacion en la lista de datos del csv




            with open(archivo, "w", newline="") as arch:
                writer = csv.writer(arch)
                writer.writerow(
                    [
                        "ruta_relativa",
                        "texto descriptivo",
                        "resolucion",
                        "tamanio",
                        "tipo",
                        "lista de tags",
                        "ultimo perfil que actualizo",
                        "ultima actualizacion",
                    ]
                )
                for elem in range(len(data)):
                    writer.writerow(data[elem])
    window.close()
