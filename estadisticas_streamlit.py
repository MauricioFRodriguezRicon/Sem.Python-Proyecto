import pandas as pd
import streamlit as st
import altair as alt
import datetime as dt
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import numpy as np
import os

st.set_option('deprecation.showPyplotGlobalUse', False)
#"""Se buscan los path y se crea el dataframe para todo"""
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path,'ventanas')
path_csv = os.path.join(os.path.join(path,'csv'),'logs.csv')
path_perfiles =  os.path.join(os.path.join(path,'json'),'perfiles.json')
data_set = pd.read_csv(path_csv, encoding='utf-8')


def calcular_dias():
    #"""Se separa la columna de fecha y hora"""
    dias = data_set['Fecha y hora']
    #"""Se modifica el formato para que recupere el dia"""
    dias = pd.to_datetime(dias,dayfirst=True)
    dias = dias.dt.strftime('%A').value_counts()
    #"""Se renombra para el label"""
    dias = dias.rename('Operaciones')
    #"""Se muestra el grafico de barras pordia"""
    st.bar_chart(dias)





def buscar_genero(alias):
    #"""Busca los perfiles y separa el que tenga un alias igual que el que recibe por parametro"""
    perfiles = pd.read_json(path_perfiles)
    print(perfiles)
    busqueda = perfiles.loc[:, 'alias'] == alias
    perfiles = perfiles.loc[busqueda]
    #"""Depediendo si 'esOtroGenero' es true o false retorna o el genero o que otro genero"""
    if(perfiles['esOtroGenero'].values):
        devolver = perfiles['queOtroGenero']
    else:
        devolver = perfiles['genero']
    return devolver.values
    


def generos():
    data_set = pd.read_csv(path_csv, encoding='utf-8')
    #"""Separa la columna de nombres del dataframe"""
    personas = data_set['Alias']
    
    #"""Para cada elemento le busca el genero y lo intercambia por el nombre"""
    for i in range(len(personas)):
        alias = personas.iloc[i]
        personas.iloc[i]= buscar_genero(alias)


    #"""Cuenta segun valores iguales"""
    personas = personas.value_counts()   
    
    #"""Se crea el grafico de torta"""
    grap = plt.pie(personas,labels=personas.keys(),counterclock=True)
    plt.title('Uso por genero')
    plt.show()
    st.pyplot()


def cantidad_por_operacion():
    #"""Se separa el tipo de opereacon"""
    cant = data_set['Operacion'].value_counts()
    cant = cant.rename('Tipo de operacion')
    cant = cant.rename_axis('Operaciones')
    st.bar_chart(cant)

def cantidad_por_nick():
    #Crea un dataframe nuevo con alias operacion y cantidad = 1 para poder contarlos
    personas = pd.DataFrame({'Alias': data_set['Alias'], 'Operacion' : data_set['Operacion'],'Cant' : 1})
    #Crea el grafico y lo muestra
    bar_chart = alt.Chart(personas).mark_bar().encode(
        x="sum(Cant):Q",
        y="Alias",
        color = "Operacion"
    )

    st.altair_chart(bar_chart,use_container_width=True)
    


def mas_usadas():
    #Separa todas las lineas que tengan en la columna operacion Generacion de meme
    imagenes_memes = data_set.loc[:,"Operacion"] == 'Generacion de meme'
    imagenes_memes = data_set.loc[imagenes_memes]
    #Separa la columna valores y hace un conteo de sus valores
    imagenes = imagenes_memes['Valores']
    imagenes = imagenes.value_counts()
    #Separa todas las lineas que tengan en la columna operacion Generacion de collage
    collages = data_set.loc[:,"Operacion"] == 'Generacion de collage'
    collages = data_set.loc[collages]
    #Crea una lista y la llena con todos los elementos que se contengan en la columna previamente separada
    imagenes_collage = []
    for i in range(len(collages)):
        palabras = collages.iloc[i][3]
        palabras = palabras.replace("[","").replace("]","").replace(",","").replace("'","")
        palabras = palabras.split()
        for j in range(len(palabras)):
            imagenes_collage.append(palabras[j])
        #Se crea un set para eliminar los repetidos y despues se pasa a lista para poder usarlo mas facilmente
        nombres = set(imagenes_collage)
        nombres = list(nombres)
        #Se crea una lista de valores y se llena con la cantidad de apariciones de cada palabra
        apariciones = []
        for i in range(len(nombres)):
            apariciones.append(imagenes_collage.count(nombres[i]))

    #Crea una serie con el conteo de apariciones y usa indice las palabras de la lista
    usos_collage = pd.Series(data=apariciones,index=nombres)

    #Separa los primeros 5 elementos(si existen) de cada archivo
    usos_collage = usos_collage.head()
    imagenes_memes = imagenes_memes.head()

    #Genera las tablas y las muestra
    st.table(imagenes)
    st.table(usos_collage)


def nube_collage():
    #Separa todas las lineas que tengan en la columna operacion el valor Generacion de collage
    collages = data_set.loc[:,"Operacion"] == 'Generacion de collage'
    collages = data_set.loc[collages]

    #Crea una lista y la llena con las palabras del titulo de los collages
    palabras_collage = []
    for i in range(len(collages)):
        palabras = str(collages.iloc[i][4])
        palabras = palabras.replace("[","").replace("]","").replace(",","").replace("'","")
        palabras = palabras.split()
        for j in range(len(palabras)):
            palabras_collage.append(palabras[j])

    #Pasa la lista a una cadena de texto
    palabras_collage = " ".join(palabras_collage)
    #Genera el grafico y lo muestra
    nube_collage = WordCloud(width=300,height=300,background_color="white",colormap="gist_rainbow_r", repeat=True).generate(text= palabras_collage)
    plt.axis("off")
    plt.imshow(nube_collage,interpolation="bilinear")
    st.pyplot()

def nube_meme():
    #Separa todas las lineas que tengan en la columna operacion el valor Generacion de meme
    memes = data_set.loc[:,"Operacion"] == 'Generacion de meme'
    memes = data_set.loc[memes]

    #Crea una lista y la llena con las palabras de los textos de los memes
    palabras_memes = []
    for i in range(len(memes)):
        palabras = memes.iloc[i][4]
        palabras = palabras.replace("[","").replace("]","").replace(",","").replace("'","")
        palabras = palabras.split()
        for j in range(len(palabras)):
            palabras_memes.append(palabras[j])
    #Pasa la lista a una cadena de texto
    palabras_memes = " ".join(palabras_memes)
    #Genera el grafico y lo muestra
    nube_memes = WordCloud(width=300,height=300,background_color="white",colormap="gist_rainbow", repeat=True).generate(text= palabras_memes)
    plt.axis("off")
    plt.imshow(nube_memes,interpolation="bilinear")
    st.pyplot()



def generacion_por_genero():
    #Baja el set nuevamente para evitar errores y separa las lineas que tengan Generacion de collage o Generacion de meme en la columna operacion
    data_set = pd.read_csv(path_csv, encoding='utf-8')
    generaciones = ["Generacion de collage","Generacion de meme"]
    total = data_set['Operacion'].isin(generaciones)
    total = data_set.loc[total].copy()

    #Separa todos los alias
    personas = total['Alias']
    
    #Para cada elemento le busca el genero y lo intercambia por el nombre
    for i in range(len(personas)):
        alias = personas.iloc[i]
        personas.iloc[i] = buscar_genero(alias)


    operaciones = personas.value_counts()
    #Genera el grafico y lo muestra
    plt.pie(operaciones,labels=operaciones.keys(),counterclock=True)
    plt.title('Generaciones por genero')
    plt.show()
    st.pyplot()

#Streamlit
st.title('Analisis de datos: Log de actividad')
st.write('Todos los cuadros se calculan utilizando el archivo de logs del sistema')

st.subheader('Actividad segun el dia de la semana')
st.write('Se separa la columna donde se encuentra la fecha y hora, despues se pasan las fechas al dia de la semana correspondiente, y posteriormente se cuentan las apariciones de cada dia')
calcular_dias()

st.subheader('Actividad por genero')
st.write('Se separa la columna de alias, se pasan todos los alias a sus respectivos generos segun el archivo perfiles.json y se cuentan las apariencias')
generos()

st.subheader('Cantidad por tipo operacion')
st.write('Se separa la columna de evento y se cuentan las apariciones de cada evento')
cantidad_por_operacion()

st.subheader('Operaciones por nick')
st.write('Se separa la columna de los alias y se cuentan las apariciones de cada nick')
cantidad_por_nick()

st.subheader('Imagenes mas usadas en collages y memes')
st.write('Se separa un dataframe con las lineas del log que tengan por evento "Generacion de meme" o "Generacion de collage", posteriormente se pasan a una lista todas las fotos que estas contengan y se cuentan las apariciones en un nuevo dataframe que contiene nombre y cantidad')
mas_usadas()


st.subheader('Nubes de palabras de los memes')
st.write('Se separan todas las lineas que en la columna evento contengan "Generacion de meme", posteriormente se crea una lista con todas las palabras, esa lista se pasa a cadena de texto y posteriormente se genera la nube de palabras')
nube_collage()

st.subheader('Nubes de palabras de los collages')
st.write('Se separan todas las lineas que en la columna evento contengan "Generacion de collage", posteriormente se crea una lista con todas las palabras, esa lista se pasa a cadena de texto y posteriormente se genera la nube de palabras')
nube_meme()

st.subheader('Generacion de collages y memes segun el genero')
st.write('Se separan las lineas que contengan "Generacion de meme" o "Generacion de collage" posteriormente se separa la columna de alias y se remplazan los alias a sus respectivos generos, despues se cuentan las apariciones de cada uno')
generacion_por_genero()