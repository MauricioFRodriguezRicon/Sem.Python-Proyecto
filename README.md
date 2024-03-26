# **UNLPIMAGE**

### Programa para la creacion de memes y collages con la capacidad de etiquetar imagenes


## Indice

* Proyecto
* Funcionamiento
* Tecnologias empleadas
* Instalacion del programa
* Dependencias
* Fuentes

## Proyecto

Este es un programa diseñado y pensado como proyecto final de la catedra "Seminario de Lenguajes - Python"
Este proyecto consiste en crear una aplicacion de escritorio multiusuario, que permita crear collages y memes, que además de generar nuevas imagenes permitirá clasificar imágenes y acceder a las imágenes almacenadas en nuestra computadora.

## Funcionamiento

El programa utiliza las imagenes .png que se encuentren en las carpetas tanto predeterminadas como definidas por el usuario. Agregando metadata como etiquetas y titulo a las imagenes, permitiendo la creacion de memes en base a plantillas predefinidas a la que se le agregan los textos deseados o la creacion de collages utilizando las imagenes etiquetadas previamente como postulantes para estos.

## Tecnologias empleadas

Para este proyecto las tecnologias empleadas fueron:
### **Lenguaje de programacion**
* ***Python 3.11.3*** para la totalidad del desarrollo del proyecto
### **Librerias**
* ***PySimpleGui***para crear las interfaces graficas
* ***Pillow*** para el manejo de imagenes
* ***Json*** para el guardado y uso de los datos referentes a los perfiles, carpetas y metadata de las imagenes
* ***Csv*** para el almacenamiento de los datos de las imagenes y logs del sistema
* ***Pandas*** para el manejo de datos en las estadisticas
* ***MathPlotLib*** para la creacion de graficos en las estadisticas
* ***Jupyter*** para la muestra de estadisticas desarrolladas en el archivo "estadisticas_jupyter.py"
* ***Streamlit*** para la exposicion de estadisticas creadas en el archivo "estadisticas_streamlit.py"

## Instalacion del programa

* **Se necesita Python 3.11.x para la ejecución del programa**

* Se precisa clonar o descargar el repositorio en la computadora 

### **Clonado**
* El clonado se puede realizar con el comando
```
git clone https://gitlab.catedras.linti.unlp.edu.ar/python2023/code/grupo09.git
```
* Por problemas proximos a solucionar debe cambiar la rama de trabajo a la rama "ENTREGA_FINAL" con el comando
```
git checkout ENTREGA_FINAL
```

### **Descarga**
* La descarga se puede realizar desde la url https://gitlab.catedras.linti.unlp.edu.ar/python2023/code/grupo09.git

* Por problemas proximos a solucionar se solicita que antes de realizar la descarga se cambie a la rama "ENTREGA_FINAL"

### **Ejecucion**

* Para ejecutar el programa debe escribir uno de los siguientes comandos dentro de la carpeta "grupo09" dependiendo de su instalacion de python
```
python unlpimage.py

python3 unlpimage.py
```

* Para acceder al archivo "estadisticas_jupyter.py" se debe abrir un jupyter notebook, con el comando mostrado a continuacion,desde la carpeta "grupo09" y posteriormente abrir el archivo
```
jupyter notebook
```

* Para abrir el archivo "estadisticas_streamlit.py", estando con la terminal en la carpeta "grupo09" se debe ejecutar el siguiente comando
```
streamlit run estadisticas_streamlit.py
```

## Dependencias

Todas las dependencias necesarias para el correcto funcionamiento del programa se encuentra en el archivo "requeriments.txt"

Puede instalar las dependencias necesarias manualmente o con el uso de uno de los comandos siguientes dependiendo de su instalacion de Python

```
pip install -r requeriments.txt

pip3 install -r requeriments.txt
```

## Fuentes

En caso de tener algun problema con las fuentes la carpeta para instalarlas se encuentra en "grupo09/ventanas/fuentes"


