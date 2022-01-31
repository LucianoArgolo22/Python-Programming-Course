#%%
import csv
from informe_funciones import leer_camion

def buscar_precio(precio_buscado):
    with open("precios.csv","rt") as f:
        data = f.read()
        filas_de_datos = []
        data = data.split("\n")
        encontrado = 0
    for fila in data:
        fila = fila.split(",")
        if precio_buscado == fila[0]:
            print(precio_buscado, fila[1])
            encontrado = 1
    if encontrado == 0:
        print(precio_buscado + " No se ha encontrado")


def costo_camion(archivo):
    records = leer_camion(archivo,tipos_datos = None)
    suma_total = 0
    for i,record in enumerate(records):
        
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            suma_total += ncajones * precio
        
        except:
            print("Fila {} : No puede interpretar {} ".format(i,fila) )
    
    return suma_total

