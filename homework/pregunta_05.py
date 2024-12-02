"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

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

df1_2 = [[item[0], item[1]] for item in df]
df1_2_tupla = [tuple(item) for item in df1_2]

result = {}

for fila in df1_2_tupla:
    letra, value = fila
    value = int(value)
    if letra not in result:
        #inicializar con el primer valor encontrado
        result[letra] ={"max" : value, "min" : value}
    else:

        #Actualizar el minimo  y máximo 
        result[letra]["max"] = max(result[letra]["max"], value)
        result[letra]["min"] = min(result[letra]["min"], value)

resultados_tuplas= [(letra, values["max"], values["min"]) for letra, values in result.items()]

resultados_tuplas = sorted(resultados_tuplas)

print(resultados_tuplas)