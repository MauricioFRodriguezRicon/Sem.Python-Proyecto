import PySimpleGUI as sg
import os
import ventanas.constantes as c
import ventanas.save_log as log
from PIL import Image, ImageTk, ImageFont ,ImageDraw

#la funcion cuadros se encarga de devolver una cierta cantidad de cuadros de textos que sean necesarios dependiendo 
#de la clave que haya sido mandada por parametro ( que seria el len(image_dict["text_boxes"]) )
def cuadros(clave):
	cuadros_text={
		1:[
			[sg.Text("TEXTO 1:", size=(20, 1),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Multiline(size=(30,4),key="-TEXT-1-")],
		  ],
		2:[
			[sg.Text("TEXTO 1:", size=(20, 1),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Multiline(size=(30,4),key="-TEXT-1-")],
			[sg.Text("TEXTO 2:", size=(20, 1),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Multiline(size=(30,4),key="-TEXT-2-")]
		  ],
		3:[
			[sg.Text("TEXTO 1:", size=(20, 1),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Multiline(size=(30,4),key="-TEXT-1-")],
			[sg.Text("TEXTO 2:", size=(20, 1),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Multiline(size=(30,4),key="-TEXT-2-")],
			[sg.Text("TEXTO 3:", size=(20, 1),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Multiline(size=(30,4),key="-TEXT-3-")]
		  ],
	}	
	return cuadros_text[clave]

def layout(cant):
	fonts = ["bahnschrift","calibri","Candara","consola","constan","georgia","impact"]
	
	color_text=["white","black"]
	
	columna_1 = [
		[
				sg.Text("Seleccione una fuente:",font=("", 13),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO),
				sg.Text("color de texto",font=("", 13),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)
			],
		[sg.Combo(fonts,default_value=["bahnschrift"], size=(22, 1), key="-FONT-", enable_events=True),sg.Combo(color_text,default_value=["black"],size=(15, 1),key="-COLOR-")],
	]+cuadros(cant)
	
	columna_2 = [
		[sg.Image(key="-IMAGEN-")]
	]
	
	button_volver=[[sg.Button("<<<Volver<<<",size=(10,2),key="-VOLVER-",button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES))]]
	button_guardar=[
			[sg.Text("nombre del archivo",font=("", 15),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[
					sg.Button("<GUARDAR>",size=(10,2),key="-GUARDAR-",button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES)),
					sg.Input(default_text="default",size=(25,2),key="-NAME-FILE-")				
				]
		]
	button_restablecer=[[sg.Button("|Restablecer|",size=(10,2),key="-RESTABLECER-",button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES))]]
	button_in=[[sg.Button("INTRODUCIR TEXTO",size=(10,2),key="-INTRODUCIR-TEXTO-",button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES))]]
	return[
		[
				sg.Column(button_volver,element_justification="left",expand_x=True,background_color=c.COLOR_FONDO),
				sg.Column(button_restablecer,expand_x=True,background_color=c.COLOR_FONDO)
			],
		[
			sg.Column(
						columna_1,
						element_justification="left",
						expand_x=True,
						size=(500,500),
						background_color=c.COLOR_FONDO,
					),
			sg.Column(
						columna_2,
						element_justification="right",
						expand_x=True,
						size=(550,550),
						background_color=c.COLOR_FONDO,
					),
		],	
		[
				sg.Column(button_in,element_justification="left",expand_x=True,background_color=c.COLOR_FONDO),
				sg.Column(button_guardar,element_justification="right",expand_x=True,background_color=c.COLOR_FONDO),
			],
	]

def edicion(meme_original,image_dict,datos_carp,user):
	
	#el tamaño de image_dict["text_boxes"] nos ayudara para sacar 
	#la cantidad de cuadros de textos necesarios para el meme
	cant_box=len(image_dict["text_boxes"])	
		
	window = sg.Window(
			"Seleccionar Fuente",
			 layout(cant_box),
			 background_color=c.COLOR_FONDO,
			 finalize=True,
			 resizable=True,
			 size=(1100,700)
		)
	
	window.set_min_size((1100,700))
	
	#creamos una copia del meme_original pasado por parametro y lo previsualizamos
	meme_copy = meme_original.copy()
	meme_tk = ImageTk.PhotoImage(meme_copy)
	window["-IMAGEN-"].update(data=meme_tk)
	###
	
	#funciones para el calculo del tamaño de la fuente
	
	def tam_box(top_x1,top_y1,bottom_x2,bottom_y2):
		return (bottom_x2-top_x1,bottom_y2-top_y1)
	
	def entra (contenedor, contenido):
		return contenido[0]<= contenedor[0] and contenido [1] <= contenedor[1]
	
	def calcular_tam_fuente(draw,texto,path_fuente,box):
		tam_contenedor =tam_box(*box)
		for tam in range(200,15, -4):
			fuente = ImageFont.truetype(path_fuente,tam)
			box_texto = draw.textbbox ((0,0),texto, font=fuente)
			tam_box_texto = tam_box(*box_texto)
			if entra(tam_contenedor, tam_box_texto):
				return fuente
		return fuente
	
	###
	
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		if event == "-FONT-":
			fuente = values["-FONT-"] 
			#usando la cant_box podemos actualizar los cuadros de textos segun la fuente elegida
			for clave in range(1,cant_box+1):
				window[f"-TEXT-{clave}-"].update(font=fuente)
		if event == "-INTRODUCIR-TEXTO-":
			#
			for clave in range(1,cant_box+1):
				textos = []
				textos.append(values[f"-TEXT-{clave}-"])
				draw =ImageDraw.Draw(meme_copy)
				path = os.path.dirname(os.path.abspath(__file__))
				path_fuente=os.path.join(path,"fuentes",f"{values['-FONT-']}.ttf")
				###
				#sacamos las coordenadas que estan en el diccionario pasado por parametro para luego 
				#calcular el tamaño de la fuente
				
				top_left_x=image_dict["text_boxes"][clave-1]["top_left_x"]
				top_left_y=image_dict["text_boxes"][clave-1]["top_left_y"]
				bottom_rigth_x=image_dict["text_boxes"][clave-1]["bottom_right_x"]
				bottom_rigth_y=image_dict["text_boxes"][clave-1]["bottom_right_y"]
				
				box = (top_left_x,top_left_y,bottom_rigth_x,bottom_rigth_y)
				
				###
				fuente_ajustada=calcular_tam_fuente(draw,values[f"-TEXT-{clave}-"],path_fuente,box)
				draw.text((top_left_x,top_left_y),values[f"-TEXT-{clave}-"],font=fuente_ajustada,fill=values["-COLOR-"])
				meme_tk = ImageTk.PhotoImage(meme_copy)
				window["-IMAGEN-"].update(data=meme_tk)
		#restablece a la imagen original y seguimos modificando solo a meme_copy
		if event == "-RESTABLECER-":
			meme_copy= meme_original.copy()
			meme_tk = ImageTk.PhotoImage(meme_copy)
			window["-IMAGEN-"].update(data=meme_tk)
		if event == "-VOLVER-":
			window.close()
			return True
		if event== "-GUARDAR-":
			valido = True

			for clave in range(1,cant_box+1):
				if(values[f"-TEXT-{clave}-"] == ""):
					valido = False
					break
			

			if (valido):
				direccion = datos_carp["meme"]
				if (os.path.isabs(direccion)):
					pass
				else:
					direccion = os.path.join(path,direccion)

				nombre_meme = os.path.join(direccion,f"{values['-NAME-FILE-']}.jpg")

				if(os.path.exists(nombre_meme)):
					sg.Popup("El nombre para el archivo ya existe por favor elija otro")
				else:
					log.registro_log(user,"Generacion de meme",image_dict['name'],textos)
					meme_copy.convert(mode="RGB").save(nombre_meme)
					sg.Popup("El meme se genero correctamente")
					break
			else:
				sg.popup("El meme necesita texto")
	window.close()
