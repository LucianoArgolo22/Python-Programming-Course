
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

        
buscar_precio("Frambuesa")
