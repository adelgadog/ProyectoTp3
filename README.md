Proyecto Tp3

Proyecto realizado para el ejercicio Tp3 de la primera evaluación de la asignatura de programación usando el lenguaje Python 3.

Requisitos mínimos.

Este script utiliza varias librerías, entre ellas solo feedparser debe ser instalada de forma independiente.

Pasos previos.

Para el correcta funcionamiento del script debes instalar la librería feedparser:

Para linux: 

$ python setup.py install

Para windows:

pip install feedparser

Objetivo del proyecto.

El código permite guardar en un archivo el título y resumen del número que queramos de los últimos trabajos actualizados de la página FictionPress.com.
El programa nos permite elegir entre tres géneros diferentes, a saber: acción, humor y horror, así como elegir el número de entradas guardadas así como el nombre del archivo destino donde se guardará.

Ejecución del proyecto.

El script se puede ejecutar de dos maneras:

Si se conocen las diferentes opciones previamente se puede introducir la elegida mediante argumento.
	
codigo.py humor

Si no se conocen las opciones previamente y no se introducen argumentos el programa pedirá el género por sí mismo.

	codigo.py
