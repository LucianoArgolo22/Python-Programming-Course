import csv
from pprint import pprint
from fileparse import parse_csv
import fileparse
from camion import Camion
from lote import Lote

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

def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(filename,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)

def leer_precios(archivo,tipos_datos = [str,float]):
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
    camion = leer_camion(archivo1)
    precios = leer_precios(archivo2)

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

def hacer_informe(camion,precios):
    lista_balances = []
    for fila in camion:
        for key_precio in precios.keys():
            if key_precio == fila.nombre:
                if isinstance(fila.precio,float):
                    lista_balances.append((fila.nombre ,int(fila.cajones),float(fila.precio),round(float(precios[key_precio]) - fila.precio,2)))
                else:
                    print("Error con el tipo de dato 'Fila'precio'' : ", type(fila["precio"]))
    return lista_balances


def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    #formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe)

def imprimir_informe(data_informe):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''
    headers = ('Nombre','Cajones','Precio','Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in data_informe:
        print('%10s %10d %10.2f %10.2f' % row)

