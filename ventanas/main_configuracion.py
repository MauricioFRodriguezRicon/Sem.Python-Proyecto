import PySimpleGUI as sg
import ventanas.layout_configuracion as c
import ventanas.save_configuracion as s
import ventanas.save_log as log
import ventanas.menu as menu


# star_configuracion crea los eventos a guardar en archivo json
def menu_configuracion(user):
    window = c.load_Configuracion()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-volver-":
            window.close()
            menu.abrir_menu(user)
        elif event == "-guardar-":
            car = {
                "imagen": value["-imagen-"],
                "collage": value["-collage-"],
                "meme": value["-meme-"],
            }
            s.save_configuracion(car)
            log.registro_log(user, "cambios en los directorios de imagenes")

    window.close()
