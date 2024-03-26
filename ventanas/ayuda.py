import PySimpleGUI as sg
import ventanas.constantes as c

"""Ventana de ayuda"""
def ayuda():
    layout = [
        [
            sg.Text(
                "Gracias por descargar esta aplicacion desarrollada por alumnos de la facultad de informatica",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "1_ En la esquina superior izquierda se encuentra el perfil del usuario actual,si te cliquea te lleva a la ventana de modificar perfil.En el caso de modificar este, reinicie la aplicacion para ver efectivo el cambio",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "2_ En la esquina superior derecha se encuentra la opcion de configuracion y la de ayuda(en la que esta en este momento).Al iniciar por primera vez la aplicacion configurar todas las rutas de carpetas para evitar errores",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "3_ En el centro se puede ver el menu compuesto de 4 items",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Etiquetar imagen_ Se le permite agregarle etiquetas a una imagen que se encuentre en el sistema",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Generar meme_ Te permite generar un meme en base a una imagen que se encuentre en el sistema.(Aun no implementada)",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Generar collage_ Te permite generar un collage en base a imagenes que se encuentren en el sistema.(Aun no implementada)",
                background_color=c.COLOR_FONDO,
            )
        ],
        [
            sg.Text(
                "Salir_ Sale del menu y vuelve a elegir perfil",
                background_color=c.COLOR_FONDO,
            )
        ],
    ]

    window = sg.Window("Info", layout, background_color=c.COLOR_FONDO, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()
