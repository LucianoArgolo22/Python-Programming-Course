import csv
from pprint import pprint
from fileparse import parse_csv


def costo_camion(archivo):
    f = open(archivo)
    
    rows = csv.reader(f)
    headers = next(rows)
    filas_de_datos = []
    i = 0
    suma_total = 0

    for fila in rows:
        filas_de_datos.append((fila[0],fila[1],fila[2]))

    for fila in filas_de_datos:
        i += 1

        try:
            suma_total += float(fila[1]) * float(fila[2])
        except:
            print("Advertencia al querer sumar string del dato de la fila: ",i )
    return suma_total,filas_de_datos,headers

def leer_camion(archivo,tipos_datos):
    """utiliza el módulo parse csv, pero transforma los tipos
    de datos para poder trabajarlos antes"""
    return parse_csv(archivo,types = tipos_datos)

def leer_precio(archivo,tipos_datos):
    """Utilizo de vuelta el módulo parse csv, pero esta vez, le 
    pido que no tenga headers, y que me transforme el tipo de datos
    además la función genera a partir de lo obtenido un diccionario
    sino el resto del programa me queda inoperante"""
    lista_tuplas = parse_csv(archivo,has_headers=False,types = tipos_datos)
    precios = {}
    for nombre,precio in lista_tuplas:
        precios[nombre] = precio
    return precios

def balances(archivo1,archivo2):
    camion = leer_camion(archivo1, tipos_datos = [str,int,float])
    precios = leer_precio(archivo2, tipos_datos = [str,float])

    balance = 0
    for fila in camion:
        for key_precio in precios.keys():
            if key_precio == fila["nombre"]:
                if isinstance(fila["precio"],float):
                    balance = ((float(precios[key_precio]) - fila["precio"]) * int(fila["cajones"]))
                    balance += balance
                else:
                    print("Error con el tipo de dato 'Fila'precio'' : ", type(fila["precio"]))

    return balance

def hacer_informe(archivo1,archivo2):
    camion =  leer_camion(archivo1, tipos_datos = [str,int,float])
    precios = leer_precio(archivo2, tipos_datos = [str,float])
    lista_balances = []
    for fila in camion:
        for key_precio in precios.keys():
            if key_precio == fila["nombre"]:
                if isinstance(fila["precio"],float):
                    lista_balances.append((fila["nombre"],int(fila["cajones"]),float(fila["precio"]),round(float(precios[key_precio]) - fila["precio"],2)))
                else:
                    print("Error con el tipo de dato 'Fila'precio'' : ", type(fila["precio"]))
    return lista_balances,list(camion[0].keys())

def imprimir_informe(archivo1,archivo2):
    informe,headers = hacer_informe(archivo1,archivo2)
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {"cambio":>10s}')
    print('---------- ---------- ---------- ----------')
    for r in informe:
        print(f'{r[0]:>10s} {r[1]:>10d} {"$"+str(r[2]):>10s} {r[3]:>10.2f}')

def informe_camion(archivo1,archivo2):
    imprimir_informe(archivo1,archivo2)

