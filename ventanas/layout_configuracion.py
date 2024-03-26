import PySimpleGUI as sg
import os
import json

import ventanas.constantes as c  # Los colores que usamos para los botones,etc


def load_Configuracion():
    # seleccionamos las carpetas donde estan las Imagenes
    # y donde se guardaran los collge y memes

    ruta_json = os.path.join(os.path.dirname(__file__), "json")
    ruta_json = os.path.join(ruta_json, "carpetas.json")

    with open(ruta_json, encoding="utf-8") as arch:
        arch.seek(0)
        carpetas = arch.read()
        carpetas = json.loads(carpetas)

    layout = [
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            "Configuración",
                            font=("", 20),
                            text_color=c.COLOR_TEXTO,
                            background_color=c.COLOR_FONDO,
                        )
                    ]
                ],
                background_color=c.COLOR_FONDO,
                element_justification="left",
                justification="left",
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.Button(
                            button_text="<Volver",
                            font=("", 10),
                            button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                            pad=(32, 34),
                            key="-volver-",
                        )
                    ]
                ],
                background_color=c.COLOR_FONDO,
                element_justification="right",
                justification="right",
            )
        ],
        [
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Text(
                "Repocitorio de imagenes",
                pad=(12, 22),
                font=(12, 13),
                text_color=(c.COLOR_TEXTO),
                background_color=(c.COLOR_FONDO),
                key="-pantalla-",
                expand_x=True,
            ),
            sg.Push(background_color=c.COLOR_FONDO),
        ],
        [
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Input(
                default_text=carpetas["imagen"],
                disabled=True,
                key="-imagen-",
                font=(12, 12),
            ),
            sg.FolderBrowse(
                button_text="Seleccionar", button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES)
            ),
            sg.Push(background_color=c.COLOR_FONDO),
        ],
        [
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Text(
                "Directorio de Collage",
                pad=(12, 22),
                font=(12, 13),
                text_color=(c.COLOR_TEXTO),
                background_color=c.COLOR_FONDO,
                expand_x=True,
            ),
            sg.Push(background_color=c.COLOR_FONDO),
        ],
        [
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Input(
                default_text=carpetas["collage"],
                disabled=True,
                key="-collage-",
                font=(12, 12),
            ),
            sg.FolderBrowse(
                button_text="Seleccionar", button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES)
            ),
            sg.Push(background_color=c.COLOR_FONDO),
        ],
        [
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Text(
                "Directorio de Memes",
                pad=(12, 22),
                font=(12, 13),
                text_color=(c.COLOR_TEXTO),
                background_color=c.COLOR_FONDO,
                expand_x=True,
            ),
            sg.Push(background_color=c.COLOR_FONDO),
        ],
        [
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Input(
                default_text=carpetas["meme"],
                disabled=True,
                key="-meme-",
                font=(12, 12),
            ),
            sg.FolderBrowse(
                button_text="Seleccionar", button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES)
            ),
            sg.Push(background_color=c.COLOR_FONDO),
        ],
        [
            sg.Column(
                [
                    [
                        sg.Button(
                            button_text="Guardar",
                            button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                            font=("", 10),
                            pad=(32, 34),
                            expand_x=True,
                            key="-guardar-",
                        )
                    ]
                ],
                background_color=c.COLOR_FONDO,
                element_justification="right",
                justification="right",
            )
        ],
    ]
    return sg.Window(
        "Configuraciones",
        layout,
        finalize=True,
        size=(1100, 700),
        background_color=(c.COLOR_FONDO),
    )
