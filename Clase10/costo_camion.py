#%%
import csv
import informe_final

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

    
def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()

