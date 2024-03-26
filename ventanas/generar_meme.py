import PySimpleGUI as sg
import json
import os
import ventanas.constantes as c
from PIL import Image, ImageTk
import ventanas.editar_meme as Edit
import ventanas.inicio as inicio

def generar(user):

	#se carga el archivo json para la ListBox de plantillas
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

	plantillas_json = os.path.join(path,"json/plantillas.json")
	with open(plantillas_json,"r")as a_json:
		datos_plant=json.load(a_json)
		
	list_datos=[p["name"] for p in datos_plant]
	
	#se carga el diccionario con los directorio de imagenes , meme, collages
	
	carpetas_json =	os.path.join(path, "json/carpetas.json")	
	with open(carpetas_json,"r")as a_json:
		datos_carp=json.load(a_json)

	#cargamos una imagen predeterminada que esta dentro del archivo del proyecto, este estara fijo
	dir_plantillas = os.path.join(path,"plantillas")
	dir_predeterminado=os.path.join(dir_plantillas,"predeterminado.png")
	meme_predeterminado = Image.open(dir_predeterminado)
	plant_seleccionado = meme_predeterminado

	def layout():
		columna_1=[
			[sg.Text("seleccionar template",font=("", 15),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Listbox(
				list_datos,
				size=(50, 10),
				enable_events=True,
				key="-LIST-BOX-",
				)
			],
			[sg.Text("",key="-TEXT-ERROR-",text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
		]
		columna_2=[
			[sg.Text("Previsualizacion",font=("", 15),text_color=c.COLOR_TEXTO,background_color=c.COLOR_FONDO)],
			[sg.Image(
					key="-MEME-",
				)
			],
		]
		
		button_volver=[[sg.Button("<<<Volver<<<",size=(10,2),key="-VOLVER-",button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES))]]
		button_generar=[[sg.Button("<<Generar>>",size=(10,3),key="-GENERAR-",button_color=(c.COLOR_TEXTO, c.COLOR_BOTONES))]]
		
		return[
			[sg.Column(layout=button_volver,expand_x=True,element_justification="left",background_color=c.COLOR_FONDO)],
			[
				sg.Column(
							columna_1,
							element_justification="left",
							expand_x=True,
							size=(500,500),
							background_color=c.COLOR_FONDO
						),
				sg.Column(
							columna_2,
							element_justification="center",
							expand_x=True,
							size=(550,550),
							background_color=c.COLOR_FONDO
						),
			],
			[sg.Column(layout=button_generar,expand_x=True,element_justification="right",background_color=c.COLOR_FONDO)],
		]
	
	window =sg.Window(
				"generar meme",
				 layout(),
				 finalize=True,
				 background_color=c.COLOR_FONDO,
				 size=(1100, 700),
				 resizable=True,
			)
			
	window.set_min_size((1100,700))
	
	#cargamos la imagen para previsualizar, plant_seleccionado de inicio es el meme_predeterminado 
	#luego ira cambiando dependiendo que imagen elija el usuario 
	previsualizado= ImageTk.PhotoImage(plant_seleccionado)
	window["-MEME-"].update(data=previsualizado)

	while True:
		event,values=window.read()
		if event == sg.WIN_CLOSED:
			break
		if event == "-LIST-BOX-":
			#image_select toma el diccionario de la imagen seleccionada ya que sus claves luego seran utilizadas
			#para encontrar el archivo o usar las coordenadas de la caja de texto
			for diccionario in datos_plant:
				if values['-LIST-BOX-'][0] in diccionario["name"]:
					image_select=diccionario
			#una vez conseguir el diccionario , usando la clave 'image' sacamos el nombre del archivo
			#y concatenamos con el directorio de imagenes , y verificamos si existe dicha imagen elegida
			plant_pre = os.path.join(os.path.join(dir_plantillas,image_select['image']))
			try:
				#en caso de no existir plant_seleccionado vuelve a mostrar la imagen predeterminada
				#esto fue para evitar que cargara una imagen con un diccionario erroneo
				if not os.path.isfile(plant_pre):
					plant_seleccionado =meme_predeterminado
					previsualizado= ImageTk.PhotoImage(plant_seleccionado)
					window["-MEME-"].update(data=previsualizado)
					raise FileNotFoundError("El archivo no existe en el repositorio de imagenes actual")
			except FileNotFoundError as e:
				window["-TEXT-ERROR-"].update(e,font=("", 15))
			else:				
				plant_seleccionado = Image.open(plant_pre)
				previsualizado=ImageTk.PhotoImage(plant_seleccionado)
				window["-TEXT-ERROR-"].update("")
				window["-MEME-"].update(data=previsualizado)
		if event == "-VOLVER-":
			window.close()
			inicio.run()
		if event == "-GENERAR-":
			#verifica si la plant_seleccionado sigue siendo el meme_predeterminado ya que puede cambiar por el evento de "-LIST-BOX-"
			#ya que sino genera una imagen con un diccionario que no le corresponde
			if meme_predeterminado != plant_seleccionado:
				Edit.edicion(plant_seleccionado,image_select,datos_carp,user)
			else:
				window["-TEXT-ERROR-"].update("no puedes generar hasta elegir una plantilla \nla actual es una predeterminada sin valor",font=("", 15))
	window.close()
