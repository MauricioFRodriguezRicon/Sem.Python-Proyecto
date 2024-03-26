import PySimpleGUI as sg
import ventanas.constantes as c
import ventanas.seleccionar_modelo as s
import ventanas.menu as menu
def boton_volver():
    layout = [
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            "Generar Collage",
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
                            pad=(20, 70),
                            button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                            key="-volver-",
                            font=(11, 14),
                        )
                    ]
                ],
                background_color=c.COLOR_FONDO,
                element_justification="right",
                justification="right",
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.Button(
                            button_text=('Seleccionar Diceño de Collage'),
                            pad=(20,70),
                            button_color=(c.COLOR_TEXTO,c.COLOR_BOTONES),
                            key='-MODELO-',
                            font=(500,14),
                        )
                    ]
                ],background_color=c.COLOR_FONDO,
                element_justification='left',
                justification='left',
        
            )
        ]

    ]
    return layout
def run(user):
    user_collage=user
    window = sg.Window(
        "Generar Collage",
        boton_volver(),
        background_color=c.COLOR_FONDO,
        finalize=True,
        size=(1100, 700))
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED :
            break
        elif  event == "-volver-":
           window.close()
           menu.abrir_menu(user)
        elif event == '-MODELO-':
            window.close()
            s.run(user)
    window.close()
    