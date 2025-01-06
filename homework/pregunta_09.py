"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

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
    
    col5 = [row[4] for row in df]

    # Crear un diccionario para contar las claves
    key_counts = {}
    
    # Procesar cada registro en la columna 5
    for r in col5:
        pares = r.split(",")  # Dividir los pares clave:valor
        for pares in pares:
            key = pares.split(":")[0]  # Obtener la clave (antes de ":")
            key_counts[key] = key_counts.get(key, 0) + 1
    
    sorted_key_counts = dict(sorted(key_counts.items()))
        

    return(sorted_key_counts)


print(pregunta_09())