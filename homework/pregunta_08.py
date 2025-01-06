"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
    
    

    # Diccionario para almacenar resultados
    result = {}

    for row in df:
        col1 = row[0]  # Letra (columna 1)
        col2 = int(row[1])  # Valor único de la columna 2
    
        if col2 not in result:
            result[col2] = set()
        result[col2].add(col1)
            
        # Convertir resultados a una lista de tuplas
    output = sorted((k, sorted(list(v))) for k, v in result.items())   # Ordenar por clave
    return(output)

print(pregunta_08())