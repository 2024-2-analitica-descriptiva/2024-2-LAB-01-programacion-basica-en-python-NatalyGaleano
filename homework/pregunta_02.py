"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
import csv
import os
from collections import Counter

#Leer archivo
df = open("files/input/data.csv","r").readlines()

#1. Limpiar los datos

# Remplazar  salto de línea y separar data para poder tener una lista de listas
df = [z.replace('\n', '')for z in df]
df = [z.split("\t") for z in df]

segunda_columna = [fila[0] for fila in df]
contador = Counter(segunda_columna)
contador_ordenado = sorted(contador.items(), key=lambda x: x[0], reverse=False)
print(contador_ordenado)
