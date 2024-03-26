import PySimpleGUI as sg
import os
import ventanas.constantes as c
from ventanas.usuario import Usuario
import ventanas.main_configuracion as conf
import ventanas.modificar_perfil as mod
import ventanas.ayuda as info
import ventanas.collage_interfaz as collage
import json
from PIL import Image, ImageDraw, ImageTk
import tempfile
import io
import ventanas.etiquetar_imagenes as e
import ventanas.generar_meme as g

"""Funcion para hacer una imagen circular para mostrar en el perfil"""


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


# Redimensiona la imagen para que se pueda mostrar como boton sin perder informacion

"""Funcion que reajusta el tamaño de las fotos de ajustes"""


def resize_image(image_path, target_size):
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size
    aspect_ratio = min(target_size[0] / width, target_size[1] / height)
    new_width = int(width * aspect_ratio)
    new_height = int(height * aspect_ratio)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image

# Crea la ventana menu
def abrir_menu(user):
    ruta_json = os.path.join(os.path.dirname(__file__), "json")
    ruta_json = os.path.join(ruta_json, "perfiles.json")
    """Se bajan los datos del json para poder trabajar"""
    with open(ruta_json, encoding="utf-8") as arch:
        arch.seek(0)
        lista_usuarios = arch.read()
        lista_usuarios = json.loads(lista_usuarios)
        """Se crea un objeto usuario"""
        ingresado = Usuario(
            lista_usuarios[user]["alias"],
            lista_usuarios[user]["nombre"],
            lista_usuarios[user]["edad"],
            lista_usuarios[user]["genero"],
            lista_usuarios[user]["esOtroGenero"],
            lista_usuarios[user]["queOtroGenero"],
            lista_usuarios[user]["imagen"],
            lista_usuarios[user]["pos"],
        )

    # Se asignan las rutas
    ruta_absoluta = os.path.abspath(os.path.dirname(__file__))
    ruta_imagen = os.path.join(ruta_absoluta, "assets")
    ruta_ajustes = os.path.join(ruta_imagen, "settings.png")
    ruta_info = os.path.join(ruta_imagen, "info.png")

    # Codifica las imagenes para que se puedan mostrar sin errores
    imagen_ajustes = resize_image(ruta_ajustes, (150, 150))
    ajustes_bytes = io.BytesIO()
    imagen_ajustes.save(ajustes_bytes, format="PNG")
    imagen_info = resize_image(ruta_info, (90, 90))
    info_bytes = io.BytesIO()
    imagen_info.save(info_bytes, format="PNG")
    ajustes_bytes.seek(0)
    info_bytes.seek(0)

    # Se busca la ruta de la foto de perfil
    ruta_perfil = os.path.join(ruta_absoluta, "avatars")
    ruta_foto = os.path.join(ruta_perfil, ingresado.get_foto)

    """Se declaran las zonas del layout por separados para luego unirlas de forma que mantengan un formato"""

    # Layout correspondiente al perfil
    perfil = [
        [
            sg.Button(
                image_filename=hacer_imagen_circular(ruta_foto),
                image_size=(150, 150),
                button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                image_subsample=2,
                border_width=0,
                key="-PERFIL_FOTO-",
            )
        ],
        [
            sg.Button(
                ingresado.get_alias,
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                key="-PERFIL-",
            )
        ],
    ]
    perfil = [[sg.Column(perfil, background_color=c.COLOR_FONDO)]]

    # Layout correspondiente a los ajustes y la informacion
    opciones = [
        [
            sg.Button(
                image_data=ajustes_bytes.read(),
                image_size=(150, 150),
                image_subsample=2,
                border_width=0,
                pad=(0, 0),
                button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                key="-AJUSTES-",
            ),
            sg.Button(
                image_data=info_bytes.read(),
                image_size=(150, 150),
                border_width=0,
                pad=(0, 0),
                button_color=(c.COLOR_FONDO, c.COLOR_FONDO),
                key="-INFO-",
            ),
        ]
    ]

    # Layout correspondiente al menu
    menu = [
        [
            sg.Button(
                "Etiquetar imagenes",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=("", 19),
                pad=(30, 20),
                key="-ETIQUETAR-",
            )
        ],
        [
            sg.Button(
                "Generar meme",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=("", 19),
                pad=(30, 20),
                key="-MEME-",
            )
        ],
        [
            sg.Button(
                "Generar collage",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=("", 19),
                pad=(30, 20),
                key="-COLLAGE-",
            )
        ],
        [
            sg.Button(
                "Salir",
                button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES),
                font=("", 19),
                pad=(30, 20),
            )
        ],
    ]
    menu = [[sg.Column(menu, background_color=c.COLOR_FONDO, expand_x=True)]]

    # Se asignan tanto el perfil como las opciones en la misma linea
    superior = [
        [
            sg.Column(perfil, background_color=c.COLOR_FONDO),
            sg.Push(background_color=c.COLOR_FONDO),
            sg.Column(opciones, background_color=c.COLOR_FONDO),
        ]
    ]
    """Union final de los layout"""
    # Layout final
    layout = [
        superior,
        [sg.Column(menu, justification="center", background_color=c.COLOR_FONDO)],
    ]

    window = sg.Window(
        "UNLP-Image",
        layout,
        background_color=c.COLOR_FONDO,
        finalize=True,
        size=(1100, 700),
    )

    while True:
        event, values = window.read()
        if (event == sg.WIN_CLOSED or event == "Salir"):  # Si se clickea la 'X' o en 'Salir' se cierra la ventana
            break
        elif event == "-AJUSTES-":
            window.close()
            conf.menu_configuracion(user)
        elif event == "-INFO-":
            info.ayuda()
        elif event == "-PERFIL-" or event == "-PERFIL_FOTO-":
            mod.abrir_modificar(user)
            with open(ruta_json, encoding="utf-8") as arch:
                arch.seek(0)
                lista_usuarios = arch.read()
                lista_usuarios = json.loads(lista_usuarios)
            ingresado.actualizar(
                lista_usuarios[user]["alias"],
                lista_usuarios[user]["nombre"],
                lista_usuarios[user]["edad"],
                lista_usuarios[user]["genero"],
                lista_usuarios[user]["esOtroGenero"],
                lista_usuarios[user]["queOtroGenero"],
                lista_usuarios[user]["imagen"],
            )
            ruta_foto = os.path.join(ruta_perfil, ingresado.get_foto)
            window["-PERFIL-"].update(ingresado.get_alias)
            window["-PERFIL_FOTO-"].update(
                image_filename=hacer_imagen_circular(ruta_foto),
                image_size=(150, 150),
                image_subsample=2,
            )
        elif event == "-COLLAGE-":
            window.close()
            collage.run(user)
        elif event == "-MEME-":
            window.close()
            g.generar(user)
        elif event == "-ETIQUETAR-":
            window.close()
            e.ventana_etiquetas(user,ingresado.get_pos)
    window.close()
