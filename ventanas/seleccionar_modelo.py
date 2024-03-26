import PySimpleGUI as sg
import ventanas.constantes as c
import ventanas.generar_collage as g
import ventanas.menu as menu
import tempfile
import os
from PIL import Image


def seleccionar_modelo():
    layout1 = [
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            "Seleccionar Diseño",
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
                            button_text=("<Volver"),
                            button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                            font=(11, 14),
                            key=("-VOLVER-"),
                        )
                    ]
                ],
                background_color=c.COLOR_FONDO,
                element_justification="right",
                justification="right",
            )
        ],
    ]
    ruta_proyecto = os.path.abspath(os.path.dirname(__file__))
    imagenes = os.path.join(ruta_proyecto, "design")

    def hacer_diceño(ruta):
        imag_diceño = Image.open(ruta)
        ima = Image.new("RGB", imag_diceño.size, color="white")
        ima.paste(imag_diceño)
        with tempfile.NamedTemporaryFile(delete=False) as f:
            ima.save(f.name, format="PNG")
            ima = f.name
        return ima

    layout2 = [
        sg.Column(
            [
                [
                    sg.Button(
                        image_filename=hacer_diceño(os.path.join(imagenes, "d1.jpg")),
                        image_size=(100, 100),
                        button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                        border_width=0,
                        image_subsample=2,
                        key="-A-",
                    ),
                    sg.Button(
                        image_filename=hacer_diceño(os.path.join(imagenes, "d2.jpg")),
                        image_size=(100, 100),
                        button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                        border_width=0,
                        image_subsample=2,
                        key="-B-",
                    ),
                    sg.Button(
                        image_filename=hacer_diceño(os.path.join(imagenes, "d3.jpg")),
                        image_size=(100, 100),
                        button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                        border_width=0,
                        image_subsample=2,
                        key="-C-",
                    ),
                    sg.Button(
                        image_filename=hacer_diceño(os.path.join(imagenes, "d4.jpg")),
                        image_size=(100, 100),
                        button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                        border_width=0,
                        image_subsample=2,
                        key="-D-",
                    ),
                ]
            ],
            background_color=c.COLOR_FONDO,
            element_justification="felt",
            justification="left",
        )
    ]
    todo = [[layout1, layout2]]
    return todo


# generar collage------------------------------


def run(user):
    window = sg.Window(
        "Seleccionar Diseño",
        seleccionar_modelo(),
        background_color=c.COLOR_FONDO,
        finalize=True,
        size=(1100, 700),
    )
    while True:
        event, value = window.read()
        if (event == "-VOLVER-") :
            window.close()
            menu.abrir_menu(user) # vuelve al menu principal
        elif event == sg.WINDOW_CLOSED:
            break
        elif event == "-A-":
            window.close()
            g.generar_collageA(user)
        elif event == "-B-":  
            window.close()
            g.generar_collageB(user)
        elif event == "-C-":
            window.close()
            g.generar_collageC(user)
        elif event == "-D-": 
            window.close()
            g.generar_collageD(user)
    window.close()
