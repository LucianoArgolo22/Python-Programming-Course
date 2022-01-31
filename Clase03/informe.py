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
    suma_total = 0

    for fila in rows:
        filas_de_datos.append(fila)

    for i,fila in enumerate(filas_de_datos):
        record = dict(zip(headers, fila))
        
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            suma_total += ncajones * precio
        
        except:
            print("Fila {} : No puede interpretar {} ".format(i,fila) )
    return suma_total



#%%

if __name__ == '__main__':

    try:
        print(costo_camion(r"..\Data\fecha_camion.csv"))

    except:
        raise Exception
