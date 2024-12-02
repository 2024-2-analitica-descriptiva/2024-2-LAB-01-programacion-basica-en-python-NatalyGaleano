"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""




def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    # Importar CSV
    import csv
    import os

    # Leer el archivo csv
    df = open("files/input/data.csv", "r").readlines()

    # 1. Limpiar los datos
    # Remplazar salto de línea y separar data para poder tener una lista de listas
    df = [z.replace('\n', '') for z in df]
    df = [z.split("\t") for z in df]

    # Realizar suma
    Suma_total = 0
    for fila in df:
        Suma_total += int(fila[1])

    # Regresar la suma total
    return Suma_total
print(pregunta_01())
