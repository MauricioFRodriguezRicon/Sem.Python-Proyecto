import PySimpleGUI as sg
import ventanas.constantes as c
import ventanas.nuevo_perfil as np
import os
import json
from PIL import Image, ImageDraw
import tempfile
import ventanas.menu as menu
import ventanas.verificacion as ve

def run():
    ve.verificar()
    ruta_json = os.path.join(os.path.dirname(__file__), "json")
    ruta_json = os.path.join(ruta_json, "perfiles.json")

    # pongo los datos del json en una lista para que al querer ver mas usuarios o entrar a tu usuario se actualice en la ventana
    with open(ruta_json, "r", encoding="utf-8") as arch:
        arch.seek(0)
        contenido = arch.read()
        datos = json.loads(contenido)

    def hacer_imagen_circular(ruta):
        # Abre la imagen utilizando PIL
        image = Image.open(ruta)

        # Crea una nueva imagen en blanco con un canal alfa (transparente)
        imagen_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

        # Crea un objeto de dibujo para dibujar en la nueva imagen
        draw = ImageDraw.Draw(imagen_circular)

        # Obtén las dimensiones de la imagen
        width, height = image.size

        # Calcula el radio del círculo
        radio = min(width, height) // 2

        # Calcula el centro del círculo
        center_x = width // 2
        center_y = height // 2

        # Dibuja un círculo blanco en el objeto de dibujo
        draw.ellipse(
            (center_x - radio, center_y - radio, center_x + radio, center_y + radio),
            fill=(255, 255, 255, 255),
        )

        # Utiliza la máscara del círculo para recortar la imagen original
        imagen_circular.paste(image, mask=imagen_circular)

        # Guarda la imagen circular en un archivo temporal ya que el 'image_filename' espera una cadena de caracteres debo pasarlo a string para que me lo lea
        with tempfile.NamedTemporaryFile(delete=False) as f:
            imagen_circular.save(f.name, format="PNG")
            ruta_temporal = f.name

        # Devuelve la ruta del archivo temporal
        return ruta_temporal

    # creo 2 layout para separar en la pantalla
    layout_1 = [
        [
            sg.Text(
                "UNLPImage",
                text_color=c.COLOR_TEXTO,
                background_color=c.COLOR_FONDO,
                font=(15),
            )
        ]
    ]
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_fotos = os.path.join(ruta_actual, "avatars")

    i = 0
    layout_2 = [
        [
            sg.Button(
                image_filename=hacer_imagen_circular(
                    os.path.join(ruta_fotos, datos[i]["imagen"])
                ),
                image_size=(100, 100),
                button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                image_subsample=2,
                border_width=0,
                key="-USUARIO1-",
            ),
            sg.Button(
                image_filename=hacer_imagen_circular(
                    os.path.join(ruta_fotos, datos[i + 1]["imagen"])
                ),
                image_size=(100, 100),
                button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                image_subsample=2,
                border_width=0,
                key="-USUARIO2-",
            ),
            sg.Button(
                image_filename=hacer_imagen_circular(
                    os.path.join(ruta_fotos, datos[i + 2]["imagen"])
                ),
                image_size=(100, 100),
                button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                image_subsample=2,
                border_width=0,
                key="-USUARIO3-",
            ),
            sg.Button(
                button_text="+",
                key="-NUEVO-",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=(15),
            ),
        ],
        [
            sg.Button(
                button_text="ver mas >",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=(15),
                key="-VER-MAS-",
            )
        ],
        [
            sg.Text(
                key="-NO-USUARIOS-",
                text_color=c.COLOR_ERROR,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
        ],
    ]

    # pongo los layout creados en columnas para su manejo
    columna_1 = [
        sg.Column(
            layout_1,
            background_color=c.COLOR_FONDO,
            element_justification="left",
            expand_x=True,
            expand_y=True,
        )
    ]
    columna_2 = [
        sg.Column(
            layout_2,
            background_color=c.COLOR_FONDO,
            element_justification="center",
            expand_x=True,
            expand_y=True,
        )
    ]
    layout = [[columna_1, columna_2]]
    # creamos el objeto ventana
    window = sg.Window(
        "INICIO",
        layout,
        background_color=c.COLOR_FONDO,
        resizable=False,
        size=(1100, 700),
    )

    # un loop infinito para procesar los eventos de la ventana
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break
        elif event == "-NUEVO-":
            ven_perfil = (
                np.ventana_perfil(i)
            )  # activo la ventana de nuevo perfil si se apreta el boton 'nuevo'
            # ven_perfil.read()
            if (
                not ven_perfil
            ):  # Si la segunda ventana devuelve False, no continuar el loop
                break
            else:  # Si la segunda ventana devuelve True, continuar el loop
                continue
        elif event == "-VER-MAS-":
            if i >= len(datos):
                i = 0
            else:
                i = i + 1

            if i < len(datos):
                window["-USUARIO1-"].Update(
                    image_filename=hacer_imagen_circular(
                        os.path.join(ruta_fotos, datos[i]["imagen"])
                    ),
                    image_size=(100, 100),
                    button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                    image_subsample=2,
                )
            if (i + 1) < len(datos):
                window["-USUARIO2-"].Update(
                    image_filename=hacer_imagen_circular(
                        os.path.join(ruta_fotos, datos[i + 1]["imagen"])
                    ),
                    image_size=(100, 100),
                    button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                    image_subsample=2,
                )
            if (i + 2) < len(datos):
                window["-USUARIO3-"].Update(
                    image_filename=hacer_imagen_circular(
                        os.path.join(ruta_fotos, datos[i + 2]["imagen"])
                    ),
                    image_size=(100, 100),
                    button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                    image_subsample=2,
                )

        elif event == "-USUARIO1-":
            window.close()
            menu.abrir_menu(i)
        elif event == "-USUARIO2-":
            window.close()
            menu.abrir_menu(i + 1)
        elif event == "-USUARIO3-":
            window.close()
            menu.abrir_menu(i+2)
    window.close()
