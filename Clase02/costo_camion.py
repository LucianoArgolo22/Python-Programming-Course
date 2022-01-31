#%%
import csv


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
    f = open(archivo)
    rows = csv.reader(f)
    headers = next(rows)
    filas_de_datos = []
    i = 0
    suma_total = 0

    for fila in rows:
        filas_de_datos.append(fila)

    for fila in filas_de_datos:
        i += 1
        try:
            suma_total += float(fila[1]) * float(fila[2])
        except:
            print("Error al querer sumar string del dato de la fila: ",i )
    return suma_total


#%%

if __name__ == '__main__':

    try:
        print(costo_camion(r"..\Data\camion.csv"))

    except:
        raise Exception
