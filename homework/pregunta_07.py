"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

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
            result[col2] = []
        result[col2].append(col1)
            
        # Convertir resultados a una lista de tuplas
    output = sorted(result.items())  # Ordenar por clave
    return(output)

print(pregunta_07())