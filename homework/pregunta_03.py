"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
import csv
import os
from collections import defaultdict

#Leer archivo
df = open("files/input/data.csv","r").readlines()

#1. Limpiar los datos

# Remplazar  salto de línea y separar data para poder tener una lista de listas
df = [z.replace('\n', '')for z in df]
df = [z.split("\t") for z in df]

suma_por_letra = defaultdict(int)
for fila in df:
    letra_columna = fila[0]
    cantidad = int(fila[1])
    suma_por_letra[letra_columna] += cantidad

Ordenado = sorted(suma_por_letra.items())

print(Ordenado)