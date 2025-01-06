"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    import csv
    import os
    from collections import defaultdict

    # Leer archivo
    with open("files/input/data.csv", "r") as file:
        df = file.readlines()

    # Crear un diccionario para acumular los valores

    sumas = defaultdict(int)
    
    for linea in df:
        # Eliminar espacios extraños al principio y final de la línea
        linea = linea.strip()
        
        # Dividir la línea por tabulaciones
        columnas = linea.split("\t")

        letra_columna_1 = columnas[0]

        Valor_columna_5 = [int(x.split(":")[1]) for x in columnas[4].split(",")]
        suma_columna_5 = sum( Valor_columna_5)
        
        sumas[letra_columna_1] += suma_columna_5

    resultado = dict(sorted(sumas.items()))

    return (resultado)
    
print(pregunta_12())