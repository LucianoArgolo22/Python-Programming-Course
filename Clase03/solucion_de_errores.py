#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de "TypeError: object of type 'int' has no len()" y estaba ubicado en la línea 7.
#Lo corregí cambiando esto por aquello.
#A continuación va el código corregido

def tiene_a(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1


tiene_a('UNSAM 2020')

tiene_a('abracadabra')

tiene_a('La novela 1984 de George Orwell')

tiene_a(0)


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario 1: El error era de "SyntaxError: invalid syntax" y estaba ubicado en la línea 36, 40 y 41
#Comentario 2: El error era de "NameError: name 'Falso' is not defined" y estaba ubicado en la línea 44
#Lo corregí cambiando agregando ":" donde faltaban, y el if, el else y cambiar el "Falso" por "False"

def tiene_a(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

#
tiene_a('UNSAM 2020')
#
tiene_a('La novela 1984 de George Orwell')
# %%
#Ejercicio 3.3
#Comentario 1: El error era de "Object not iterable"
#Lo corregí agregando una línea de código en la línea 64, volviendo los números como strings, y de esa forma volverlos iterables
#Además tuve que volver la variable un str, para que pudiera iterarse sobre él 


def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
#%%
#Ejercicio 3.4
#Comentario 1: El error era el resultado
#Lo corregí agregando una línea de código en la línea 82, usando un "return", para que devuelva un valor



def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
repr(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.4
#Comentario 1: El error era ValueError: could not convert string to float: ''
#Lo corregí agregando una línea de código en la línea 64, usando un try except, para aquellos valores que 
#están vacíos, y poniendo un 0 en su lugar 
#Además tuve que mover el diccionario "registro={}" de la línea
#104, a la 107, dado que sino no se reiniciaba el valor, sino que pisaban los valores anteriores 


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])

            try:
                registro[encabezado[2]] = float(fila[2])
            except:
                registro[encabezado[2]] = 0

            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
