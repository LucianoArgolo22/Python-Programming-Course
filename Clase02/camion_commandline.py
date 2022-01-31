#%%
import csv
import sys



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


if __name__ == '__main__':

    try:
        if len(sys.argv) == 2:
            archivo = sys.argv[1]
        else:
            archivo = '..\Data\camion.csv'

        costo = costo_camion(archivo)
        print("costo total: ", costo)

    except:
        raise Exception
