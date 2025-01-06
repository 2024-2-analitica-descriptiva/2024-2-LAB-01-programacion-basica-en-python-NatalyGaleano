"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


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
        
        # Obtener el valor de la columna 2 como entero
        valor_columna_2 = int(columnas[1])
        
        # Obtener las letras de la columna 4
        letras_columna_4 = columnas[3].split(",")
        
        # Sumar el valor a cada letra en el diccionario
        for letra in letras_columna_4:
            sumas[letra] += valor_columna_2
    
    # Convertir el diccionario a un diccionario ordenado por clave
    resultado = dict(sorted(sumas.items()))
    
    return (resultado)

print(pregunta_11())
    