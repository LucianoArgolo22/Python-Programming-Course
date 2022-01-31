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
    return suma_total,filas_de_datos,headers

def leer_camion(archivo):
    suma_total,filas_de_datos,headers = costo_camion(archivo)
    lista_diccionarios = []
    for fila in filas_de_datos:
        try:
            diccionario_camion = {"nombre": fila[0], "cajones": fila[1], "precio": float(fila[2])}
            lista_diccionarios.append(diccionario_camion)
        except:
            pass
    return lista_diccionarios,headers

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
    camion,headers = leer_camion(archivo1)
    precios = leer_precio(archivo2)
    lista_balances = []
    for fila in camion:
        for key_precio in precios.keys():
            if key_precio == fila["nombre"]:
                if isinstance(fila["precio"],float):
                    lista_balances.append((fila["nombre"],int(fila["cajones"]),float(fila["precio"]),round(float(precios[key_precio]) - fila["precio"],2)))
                else:
                    print("Error con el tipo de dato 'Fila'precio'' : ", type(fila["precio"]))

    return lista_balances,headers




if __name__ == '__main__':

    try:
        # balance_total = balances("..\Data\camion.csv","..\Data\precios.csv")
        # print("\n\nSe obtuvo una ganancia total de: ")
        # pprint(round(balance_total,3))
        # print("\n\nSiendo el monto por cada producto de: ")
        informe,headers = hacer_informe("..\Data\camion.csv","..\Data\precios.csv")
        print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {"cambio":>10s}')
        print('---------- ---------- ---------- ----------')
        for r in informe:
            print(f'{r[0]:>10s} {r[1]:>10d} {"$"+str(r[2]):>10s} {r[3]:>10.2f}')
    
    except:
        raise Exception

