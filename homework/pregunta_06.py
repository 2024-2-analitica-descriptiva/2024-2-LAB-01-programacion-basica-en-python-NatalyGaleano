"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
    
    df= [[item[4]] for item in df]
    df= [x[0].split(",") for x in df ]
    
    values_by_key = defaultdict(list)
    
    for row in df:
        
        for item in row:
            key, value = item.split(":")
            values_by_key[key].append(int(value))
    
    # Paso 2: Calcular el mínimo y máximo para cada clave
    results = [(key, min(values), max(values)) for key, values in values_by_key.items()]
    
    results= sorted(results)
    
    # Paso 3: Mostrar resultados
    return(results)
print(pregunta_06())



