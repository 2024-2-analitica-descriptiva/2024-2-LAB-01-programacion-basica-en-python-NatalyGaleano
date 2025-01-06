"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    import csv
    import os
    from collections import defaultdict
    
    #Leer archivo
    df = open("files/input/data.csv","r").readlines()
    
    #1. Limpiar los datos
    # 
    # Remplazar  salto de línea y separar data para poder tener una lista de listas
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t") for z in df]
    
    #Extraer el campo Fechas
    df = [z[2] for z in df[0:]]
    
    #Separar las fechas en sus partes (año, mes y día)
    meses = [date.split('-')[1] for date in df[0:]]
    
    #Cantidad de registros
    mes_contador ={}
    for mes in meses:
        if mes in mes_contador:
            mes_contador[mes] +=1
        else:
            mes_contador[mes] =1
            
    #crear una lista de tuplas
    meses_tuplas = sorted(mes_contador.items())

    return(meses_tuplas)
  
  
print(pregunta_04())
