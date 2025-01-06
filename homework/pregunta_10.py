"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    # Leer archivo
    with open("files/input/data.csv", "r") as file:
        df = file.readlines()
    
    resultado = []
    
    for linea in df:
        # Eliminar espacios extraños al principio y final de la línea
        linea = linea.strip()
        
        # Dividir la línea por tabulaciones
        columnas = linea.split("\t")
        
        # Obtener la letra de la columna 1
        letra = columnas[0]
        
        # Calcular la cantidad de elementos en la columna 4
        elementos_columna_4 = len(columnas[3].split(","))
        
        # Calcular la cantidad de elementos en la columna 5
        elementos_columna_5 = len(columnas[4].split(","))
        
        # Agregar la tupla al resultado
        resultado.append((letra, elementos_columna_4, elementos_columna_5))
    
    return resultado

print(pregunta_10())