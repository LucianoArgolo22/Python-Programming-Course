import csv
from pprint import pprint
    
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
    return suma_total,filas_de_datos

def leer_camion(archivo):
    suma_total,filas_de_datos = costo_camion(archivo)
    lista_diccionarios = []
    for fila in filas_de_datos:
        try:
            diccionario_camion = {"nombre": fila[0], "cajones": fila[1], "precio": float(fila[2])}
            lista_diccionarios.append(diccionario_camion)
        except:
            pass
    return lista_diccionarios

def leer_precio(archivo):
    with open(archivo,"rt") as f:
        data = f.read()
        filas_de_datos = []
        data = data.split("\n")
        encontrado = 0
    diccionario_precios = {}
    for fila in data:
        try:
            fila = fila.split(",")
            diccionario_precios[fila[0]] = fila[1]
        except:
            pass
    return diccionario_precios


def balances(archivo1,archivo2):
    camion = leer_camion(archivo1)
    precios = leer_precio(archivo2)
    lista_balances = []
    balance = 0
    for fila in camion:
        for key_precio in precios.keys():
            if key_precio == fila["nombre"]:
                if isinstance(fila["precio"],float):
                    balance = (float(precios[key_precio]) - fila["precio"]) * int(fila["cajones"])
                    lista_balances.append((balance,fila["cajones"],fila["nombre"]))
                    balance += balance
                else:
                    print("Error con el tipo de dato 'Fila'precio'' : ", type(fila["precio"]))

    return balance, lista_balances




if __name__ == '__main__':

    try:
        balance_total, lista_balance = balances("..\Data\camion.csv","..\Data\precios.csv")
        print("\n\nSe obtuvo una ganancia total de: ")
        pprint(round(balance_total,3))
        print("\n\nSiendo el monto por cada producto de: ")
        pprint(lista_balance)
    
    except:
        raise Exception


