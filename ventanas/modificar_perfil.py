import json
import PySimpleGUI as sg
import os
import ventanas.save_log as log
from ventanas.usuario import Usuario as us
import ventanas.constantes as c

"""Genera la ventana para modificar el perfil"""
def abrir_modificar(user):
    ruta_json = os.path.join(os.path.dirname(__file__), "json")
    ruta_json = os.path.join(ruta_json, "perfiles.json")
    """Se bajan los datos del json para trabajar con ellos"""
    with open(ruta_json) as arch:
        arch.seek(0)
        lista_usuarios = arch.read()
        lista_usuarios = json.loads(lista_usuarios)
    """Se crea objeto usuario"""
    usuario = us(
        lista_usuarios[user]["alias"],
        lista_usuarios[user]["nombre"],
        lista_usuarios[user]["edad"],
        lista_usuarios[user]["genero"],
        lista_usuarios[user]["esOtroGenero"],
        lista_usuarios[user]["queOtroGenero"],
        lista_usuarios[user]["imagen"],
        lista_usuarios[user]["pos"]
    )
    """Se generan los diferentes layout"""
    datos = [
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
        [sg.Text(usuario.get_alias, key="-ALIAS-",text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),),],
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
        [sg.Input(default_text=usuario.get_nombre, key="-NOMBRE-", enable_events=True)],
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
        [sg.Input(default_text=usuario.get_edad, key="-EDAD-")],
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
                default_value=usuario.get_genero,
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
                default=usuario.get_esOtroGenero,
                enable_events=True,
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(10),
            )
        ],
        [
            sg.Input(
                key="-OTRO-GENERO-",
                default_text=usuario.get_queOtroGenero,
                disabled=True,
            )
        ],
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
    carpeta_imagenes = os.path.abspath("ventanas")
    imagenes = os.path.join(carpeta_imagenes, "avatars")
    predeterminado = os.path.join(imagenes, usuario.get_foto)
    ruta_proyecto = os.path.abspath(os.path.dirname(__file__))
    var = os.path.relpath(predeterminado, ruta_proyecto)

    foto = [
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
            sg.Input(predeterminado, key="-IMG-", enable_events=True, size=(30)),
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

    volver = [[sg.Button("< Volver", key="-VOLVER-")]]

    mod = [sg.Column(datos, justification="center", background_color=c.COLOR_FONDO)]
    """Union final del layout"""
    layout = [mod, foto, volver]

    window = sg.Window(
        "Modificar Perfil", layout, background_color=c.COLOR_FONDO, resizable=True
    )

    while True:
        event, values = window.read()
        if (
            event == sg.WIN_CLOSED or event == "-VOLVER-"
        ):  # Si se clickea la 'X' o en 'Salir' se cierra la ventana
            break
        if event == "-GUARDAR-":
            nuevo = {
                "alias": values["-ALIAS-"],
                "nombre": values["-NOMBRE-"],
                "edad": values["-EDAD-"],
                "genero": values["-GENERO-"],
                "esOtroGenero": values["-OTRO-"],
                "queOtroGenero": values["-OTRO-GENERO-"],
                "imagen": os.path.basename(values["-IMG-"]),
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

            alias = values["-ALIAS-"]
            caract = len(alias)
            esta = False
            for (
                elem
            ) in lista_usuarios:  # chequeo si ese alias ya esta en la lista de usuarios
                if elem["alias"] == alias and lista_usuarios[user]["alias"] != alias:
                    esta = True

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
                    window["-EXISTE-"].Update("Ese alias ya existe, probar con otro!")
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
                with open(ruta_json, "w", encoding="utf-8") as arch:
                    arch.seek(0)
                    lista_usuarios[user] = nuevo
                    arch.seek(0)
                    arch.write(json.dumps(lista_usuarios, indent=4))
                log.registro_log(user,"Modificacion de perfil")
                sg.Popup("Datos guardados correctamente")
                break
    window.close()
