import PySimpleGUI as sg
import ventanas.constantes as c
import json
import os


def ventana_perfil(i):
    # creo la ventana dentro de una funcion para que pueda ser llamada desde la ventana de inicio
    layout_1 = [
        [
            sg.Text(
                "Nick o alias",
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            ),
            sg.Text(
                key="-sin-alias-",
                text_color=c.COLOR_ERROR,
                background_color=c.COLOR_FONDO,
            ),
        ],
        [sg.Input(key="-ALIAS-")],
        [
            sg.Text(
                key="-EXISTE-",
                text_color=c.COLOR_ERROR,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Nombre",
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            )
        ],
        [sg.Input(key="-NOMBRE-", enable_events=True)],
        [
            sg.Text(
                key="-n-",
                text_color=c.COLOR_ERROR,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Edad",
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            ),
            sg.Text(
                key="-SIN-EDAD-",
                text_color=c.COLOR_ERROR,
                background_color=c.COLOR_FONDO,
            ),
        ],
        [sg.Input(key="-EDAD-")],
        [
            sg.Text(
                key="-edad-",
                text_color=c.COLOR_ERROR,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Genero autopercibido",
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            )
        ],
        [
            sg.DropDown(
                ["femenino", "masculino", "nobinaro"],
                readonly=True,
                enable_events=True,
                disabled=False,
                key="-GENERO-",
                button_background_color="white",
                button_arrow_color="white",
            )
        ],
        [sg.Text(text_color=c.COLOR_ERROR, font=(5), background_color=c.COLOR_FONDO)],
        [
            sg.Checkbox(
                "Otro",
                key="-OTRO-",
                enable_events=True,
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            )
        ],
        [sg.Input("Complete el genero", key="-OTRO-GENERO-", disabled=True)],
        [
            sg.Text(
                key="-OTRO-GEN-",
                text_color=c.COLOR_ERROR,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
        ],
    ]

    # Ruta de la carpeta de imágenes dentro del proyecto
    ruta_proyecto = os.path.abspath(os.path.dirname(__file__))
    imagenes = os.path.join(ruta_proyecto, "avatars")
    predeterminado = os.path.join(imagenes, "predeterminado.png")
    var = os.path.relpath(predeterminado, ruta_proyecto)
    var2 = os.path.join("ventanas", var)

    # Obtener la lista de archivos de imágenes en la carpeta
    archivos_imagenes = [
        f
        for f in os.listdir(imagenes)
        if os.path.isfile(os.path.join(imagenes, f))
        and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    layout_2 = [
        [
            sg.Text(
                "Seleccionar avatar",
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
        [
            sg.Input(var2, key="-IMG-", enable_events=True, size=(30)),
            sg.FileBrowse(
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES), font=(" ", 10)
            ),
        ],
        [
            sg.Button(
                "Guardar",
                key="-GUARDAR-",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=(" ", 12),
                pad=(76, 30),
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
        "Nuevo Perfil",
        layout,
        background_color=c.COLOR_FONDO,
        size=(1281, 854),
        resizable=True,
    )

    # un loop infinito para procesar los eventos de la ventana
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break
        elif event == "-VOLVER-":
            window.close()
            return True

        if event == "-GUARDAR-":
            nuevo = {
                "alias": values["-ALIAS-"],
                "nombre": values["-NOMBRE-"],
                "edad": values["-EDAD-"],
                "genero": values["-GENERO-"],
                "esOtroGenero": values["-OTRO-"],
                "queOtroGenero": values["-OTRO-GENERO-"],
                "imagen": os.path.basename(values["-IMG-"]),
                "pos":i
            }

            if (values["-NOMBRE-"].isalpha()) or (
                " " in values["-NOMBRE-"]
            ):  # verifico que el campo de nombre sea solo letras
                no_nombre = True
            else:
                no_nombre = False
            if values["-EDAD-"].isalpha():  # verifico que el campo edad se solo numeros
                num = False
            else:
                num = True

            if len(values["-EDAD-"]) == 0:
                s_edad = True
            else:
                s_edad = False

            ruta_json = os.path.join(os.path.dirname(__file__), "json")
            ruta_json = os.path.join(ruta_json, "perfiles.json")

            with open(ruta_json, "a+", encoding="utf-8") as arch:
                arch.seek(0)
                contenido = arch.read()
                # verificar si el archivo está vacío
                if len(contenido) == 0:
                    # si el archivo está vacío, escribir un array JSON
                    datos = [nuevo]
                    arch.write(json.dumps(datos, indent=4))
                else:
                    arch.seek(0)
                    datos = json.loads(contenido)
                    # si el archivo no está vacío, cargar los datos existentes del archivo
                    # antes verificar si ya se encuentra en los registros
                    alias = values["-ALIAS-"]
                    caract = len(alias)
                    esta = False
                    for (
                        elem
                    ) in datos:  # chequeo si ese alias ya esta en la lista de usuarios
                        if elem["alias"] == alias:
                            esta = True

                    # esto lo hago para verificar los campos ingresados, que no esten vacios y que sean correctos
                    if (
                        (caract == 0)
                        or (esta == True)
                        or (no_nombre == False)
                        or (num == False)
                        or (s_edad == True)
                    ):  # si esta sale este mensaje de error
                        if caract == 0:
                            window["-sin-alias-"].Update("Ingrese un alias!")
                        else:
                            window["-sin-alias-"].Update(" ")

                        if esta == True:
                            window["-EXISTE-"].Update(
                                "Ese alias ya existe, probar con otro!"
                            )
                        else:
                            window["-EXISTE-"].Update(" ")

                        if no_nombre == False:
                            window["-n-"].Update("Deben ser letras!")
                        else:
                            window["-n-"].Update(" ")

                        if num == False:
                            window["-edad-"].Update("Deben ser numeros!")
                        else:
                            window["-edad-"].Update(" ")

                        if s_edad == True:
                            window["-SIN-EDAD-"].Update("Ingrese una edad!")
                        else:
                            window["-SIN-EDAD-"].Update(" ")

                    else:
                        window["-EXISTE-"].Update(" ")
                        window["-n-"].Update(" ")
                        window["-edad-"].Update(" ")
                        window["-OTRO-GEN-"].Update(" ")
                        window["-sin-alias-"].Update(" ")
                        window["-SIN-EDAD-"].Update(" ")
                        # agregar el nuevo objeto JSON a la lista de datos
                        datos.append(nuevo)
                        # volver a escribir los datos completos en el archivo JSON
                        arch.seek(0)
                        arch.truncate()
                        arch.write(json.dumps(datos, indent=4))
                        sg.Popup("Datos guardados correctamente")

        if event == "-OTRO-":
            if values["-OTRO-"]:
                window["-OTRO-GENERO-"].update(disabled=False)
                window["-GENERO-"].update(disabled=True)
            else:
                window["-OTRO-GENERO-"].update(disabled=True)
                window["-GENERO-"].update(disabled=False)

        if event == "-IMG-":
            archivo_seleccionado = values["-IMG-"]
            window["-IMAGE-"].update(filename=archivo_seleccionado)
            ruta_proyecto = os.path.abspath(os.path.dirname(__file__))
            var = os.path.relpath(archivo_seleccionado, ruta_proyecto)
            var2 = os.path.join("ventanas", var)
            window["-IMG-"].update(var2)
    window.close()
