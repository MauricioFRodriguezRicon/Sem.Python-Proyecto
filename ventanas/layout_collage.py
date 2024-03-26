import PySimpleGUI as sg
import ventanas.constantes as c
#modulo que retorna un diccionario de layout con funcionalidad del collage
def layout_collage():
   layout1=[ 
         [
            sg.Text(
                "Titulo de collage",
                text_color=c.COLOR_TEXTO,
                font=(5),
                background_color=c.COLOR_FONDO,
            )
         ],
         [
          sg.Input(key="-TITULO-",default_text=" "),
          sg.Button(button_text="Agregar",
                    font=("",12),key="-AGREGAR-",
                    button_color=(c.COLOR_TEXTO,c.COLOR_BOTONES),
                    )
         ],
         [
            sg.Text(key="-SIN TITLE-",background_color=c.COLOR_FONDO,text_color="red")
         ]
      ]
   layout2=[
      [
            sg.Frame(
                " ",
                [
                    [
                        sg.Image(
                            key="-IMAGE-",
                            size=(500, 500),
                            background_color=c.COLOR_FONDO,
                        )
                    ]
                ],
                border_width=1,
                relief="solid",
                background_color=c.COLOR_FONDO,
            )
        ],
        
        [
           sg.Column([
              [
                 sg.Button(button_text=("Guardar"),
                           font=("",14),
                           button_color=(c.COLOR_TEXTO,c.COLOR_BOTONES),
                           key="-GUARDAR-",
                           )
              ]
           ],element_justification="rigth",
           justification="rigth",
           background_color=c.COLOR_FONDO)
        ]
   ]
   layout3=[
      [
         sg.Column(
            [
               [
                  sg.Button(button_text=("< Volver"),
                            key="-VOLVER-",
                            button_color=(c.COLOR_TEXTO,c.COLOR_BOTONES),
                            font=("",14),
                   )
               ]
            ],
            element_justification="rigth",
            justification="rigth",
            background_color=c.COLOR_FONDO
         )
      ]
      
   ]
   dic_layout={
      "layout_titulo":layout1,
      "layout_frame":layout2,
      "layout_volver":layout3
   }
   return dic_layout
#modulo que une todoso los layout para el grafico para generar collage
def grafico_collage(layout_imagen,hacer):
   columna_1 = sg.Column(layout_imagen+hacer["layout_titulo"] ,background_color=c.COLOR_FONDO, pad=(80, 80))
   columna_2 = sg.Column(hacer["layout_frame"], background_color=c.COLOR_FONDO)
   columna_3 = sg.Column(hacer["layout_volver"], background_color=c.COLOR_FONDO, expand_x=True)
   columnas = sg.Column(
        [[columna_3], [columna_1, columna_2]],
        background_color=c.COLOR_FONDO,
        expand_x=True,
        expand_y=True,
    )
   layout= [[[columnas]]]
   return layout