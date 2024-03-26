import PySimpleGUI as sg
import os
import ventanas.constantes as c
import ventanas.generar_rutas_collage as grc
import ventanas.seleccionar_modelo as sm
import ventanas.layout_collage as lc
from PIL import Image ,ImageTk,ImageOps,ImageDraw
import ventanas.save_log as log
#modulo que va armando el collage con cada imagen seleccionada
def hacer_collage(window,collage,imagen,ancho,alto,y,x):
     imag_selec=grc.ruta_imagen_celeccionada(imagen) # modulo que retorna la ruta de la imagen seleccionada
     imag_selec=grc.ajusta_imagen(imag_selec,ancho,alto)# achica la imagen al(ancho ,alto) pasado por parametro
     imag_selec=ImageOps.fit(imag_selec,(ancho,alto))
     collage.paste(imag_selec,(y,x))
     imag=ImageTk.PhotoImage(collage)
     window["-IMAGE-"].update(data=imag)

# modulo que crea el  diseño de collage A
def generar_collageA(user):
   imagen=grc.ruta_directorio() # el modulo retorna los directorios seleccionados en configuracion
   data=grc.imagenes_csv()       # modulo que devuelde una lista de imageses etiquetadas
   layout1=[
      [
         sg.Text("Seleccionar Imagen 1",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A1-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 2",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
       [  
          sg.Combo(values=data,
                       font=(11,14),
                       key="-A2-",change_submits=True
                      )
       ],
         
   ]
   layout_funcioanalidad=lc.layout_collage() # modulo que retorna funcionalidad del collage
   layout=lc.grafico_collage(layout1,layout_funcioanalidad)#modulo que retorna el grafico que se mostrara en ventana
   window=sg.Window(
      "Generar Collage",
      layout,
      finalize=True,
      size=(1100,700),
      background_color=c.COLOR_FONDO)
   collage= Image.new("RGB",size=(500,500))
   while True:
      event,value=window.read()
      if event== "-VOLVER-":
         window.close()
         sm.run(user)   #buelve a seleccionar diceño
      elif event==sg.WINDOW_CLOSED:
         break
      elif event == "-A1-": 
        imag_selec=value["-A1-"]                            # tomo la imagen seleccionada
        hacer_collage(window,collage,imag_selec,500,250,1,0) #modulo que agrega la imagen seleccionada al collage
      elif event == "-A2-":                                  
        hacer_collage(window,collage,value["-A2-"],500,250,1,251)
      elif event == "-AGREGAR-":  
         if(value["-TITULO-"] != " ") :                        
           cop=collage.copy()
           grc.agregar_titulo(window,cop,value["-TITULO-"])    #modulo que agrega el tiulo en el collage
         else:
            window["-SIN TITLE-"].update("ingrese un titulo")
      elif event =="-GUARDAR-":   
         if( value["-TITULO-"] != " "):

            imagenes_collage = [value["-A1-"],value["-A2-"]]
            log.registro_log(user,"Generacion de collage",imagenes_collage,value["-TITULO-"])
            grc.guardar_collage(cop,value["-TITULO-"],imagen["collage"])# modulo que guarda el collage completo
         else:
            window["-SIN TITLE-"].update("ingrese un titulo")
   window.close()
#modulo generar diseño B
def generar_collageB(user):
   imagen=grc.ruta_directorio()
   data=grc.imagenes_csv()
   layout1=[
      [
         sg.Text("Seleccionar Imagen 1",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A1-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 2",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
       [  
          sg.Combo(values=data,
                       font=(11,14),
                       key="-A2-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 3",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A3-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 4",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
       [  
          sg.Combo(values=data,
                       font=(11,14),
                       key="-A4-",change_submits=True
                      )
       ],
        
   ]
   layout_funcioanalidad=lc.layout_collage() # modulo que retorna funcionalidad del collage
   layout=lc.grafico_collage(layout1,layout_funcioanalidad)#modulo que retorna el grafico que se mostrara en ventana
   window=sg.Window(
      "Generar Collage",
      layout,
      finalize=True,
      size=(1100,700),
      background_color=c.COLOR_FONDO)
   collage= Image.new("RGB",size=(500,500))
   while True:
      event,value=window.read()
      if event== "-VOLVER-":
         window.close()
         sm.run(user)   #vuelve a seleccionar diseño
      elif event==sg.WINDOW_CLOSED:
         break
      elif event == "-A1-":
        hacer_collage(window,collage,value["-A1-"],250,250,1,0)
      elif event == "-A2-":
        hacer_collage(window,collage,value["-A2-"],250,250,252,0)
      elif event == "-A3-":
        hacer_collage(window,collage,value["-A3-"],250,250,1,251)
      elif event == "-A4-":
        hacer_collage(window,collage,value["-A4-"],300,250,252,251)
      elif event == "-AGREGAR-":
         if( value["-TITULO-"] != " "):
            cop=collage.copy()
            grc.agregar_titulo(window,cop,value["-TITULO-"])
         else:
            window["-SIN TITLE-"].update("ingrese un titulo")
      elif event =="-GUARDAR-": 
         if( value["-TITULO-"] != " "):
            imagenes_collage = [value["-A1-"],value["-A2-"],value["-A3-"],value["-A4-"]]
            log.registro_log(user,"Generacion de collage",imagenes_collage,value["-TITULO-"])
            grc.guardar_collage(cop,value["-TITULO-"],imagen["collage"])
         else:
            window["-SIN TITLE-"].update("ingrese un titulo")
   window.close()
#mudulo que crea el diseño de collage C
def  generar_collageC(user):
   imagen=grc.ruta_directorio()
   data=grc.imagenes_csv()
   layout1=[
      [
         sg.Text("Seleccionar Imagen 1",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A1-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 2",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
       [  
          sg.Combo(values=data,
                       font=(11,14),
                       key="-A2-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 3",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A3-",change_submits=True
                      )
       ],
        
   ]
   layout_funcioanalidad=lc.layout_collage() # modulo que retorna funcionalidad del collage
   layout=lc.grafico_collage(layout1,layout_funcioanalidad)#modulo que retorna el grafico que se mostrara en ventana
   window=sg.Window(
      "Generar Collage",
      layout,
      finalize=True,
      size=(1100,700),
      background_color=c.COLOR_FONDO)
   collage= Image.new("RGB",size=(500,500))
   while True:
      event,value=window.read()
      if event== "-VOLVER-":
         window.close()
         sm.run(user)   #vuelve a seleccionar diseño
      elif event==sg.WINDOW_CLOSED:
         break
      elif event == "-A1-":
        hacer_collage(window,collage,value["-A1-"],500,250,1,0)
      elif event == "-A2-":
        hacer_collage(window,collage,value["-A2-"],250,250,1,251)
      elif event == "-A3-":
        hacer_collage(window,collage,value["-A3-"],300,250,252,251)
      elif event == "-AGREGAR-":
         if(value["-TITULO-"] != " "):
            cop=collage.copy()
            grc.agregar_titulo(window,cop,value["-TITULO-"])
         else:
            window["-SIN TITLE-"].update("ingrese un titulo")
      elif event =="-GUARDAR-": 
         if(value["-TITULO-"] != " "):
            imagenes_collage = [value["-A1-"],value["-A2-"],value["-A3-"]]
            log.registro_log(user,"Generacion de collage",imagenes_collage,value["-TITULO-"])
            grc.guardar_collage(cop,value["-TITULO-"],imagen["collage"])
         else:
             window["-SIN TITLE-"].update("ingrese un titulo")
   window.close()
#modulo que crea el diceño de collage D
def  generar_collageD(user):
   imagen=grc.ruta_directorio()
   data=grc.imagenes_csv()
   layout1=[
      [
         sg.Text("Seleccionar Imagen 1",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A1-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 2",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
       [  
          sg.Combo(values=data,
                       font=(11,14),
                       key="-A2-",change_submits=True
                      )
       ],
       [
         sg.Text("Seleccionar Imagen 3",text_color=c.COLOR_TEXTO,
                 background_color=c.COLOR_FONDO,
                 font=(11,14))
      ],
      [  
         sg.Combo(values=data,
                       font=(11,14),
                       key="-A3-",change_submits=True
                      )
       ],
        
   ]
   layout_funcioanalidad=lc.layout_collage() # modulo que retorna funcionalidad del collage
   layout=lc.grafico_collage(layout1,layout_funcioanalidad)#modulo que retorna el grafico que se mostrara en ventana
   window=sg.Window(
      "Generar Collage",
      layout,
      finalize=True,
      size=(1100,700),
      background_color=c.COLOR_FONDO)
   collage= Image.new("RGB",size=(500,500))
   while True:
      event,value=window.read()
      if event== "-VOLVER-":
         window.close()
         sm.run(user)   #vuelve a seleccionar diseño
      elif event==sg.WINDOW_CLOSED:
         break
      elif event == "-A1-":
         hacer_collage(window,collage,value["-A1-"],240,500,1,0)

      elif event == "-A2-":
         hacer_collage(window,collage,value["-A2-"],360,250,242,0)
      elif event == "-A3-":
         hacer_collage(window,collage,value["-A3-"],360,250,242,251)
      elif event == "-AGREGAR-":
         if(value["-TITULO-"] != " "):
            cop=collage.copy()
            grc.agregar_titulo(window,cop,value["-TITULO-"])
         else:
             window["-SIN TITLE-"].update("ingrese un titulo")
      elif event =="-GUARDAR-": 
         if(value["-TITULO-"] != " "):
            imagenes_collage = [value["-A1-"],value["-A2-"],value["-A3-"]]
            log.registro_log(user,"Generacion de collage",imagenes_collage,value["-TITULO-"])
            grc.guardar_collage(cop,value["-TITULO-"],imagen["collage"])
         else:
             window["-SIN TITLE-"].update("ingrese un titulo")
   window.close()