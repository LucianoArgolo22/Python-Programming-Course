#%%
import csv
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
    return suma_total, filas_de_datos, headers


def leer_camion(archivo):
    suma_total,filas_de_datos,headers = costo_camion(archivo)
    lista_diccionarios = []
    for fila in filas_de_datos:
        try:
            diccionario_camion = {"nombre": fila[0], "cajones": int(fila[1]), "precio": float(fila[2])}
            lista_diccionarios.append(diccionario_camion)
        except:
            pass
    return lista_diccionarios,headers

def leer_precios(archivo):
    with open(archivo,"rt") as f:
        data = f.read()
        diccionario_de_datos = {}
        data = data.split("\n")
    for fila in data:
        try:
            fila = fila.split(",")
            diccionario_de_datos[fila[0]] = float(fila[1])
        except:
            pass
    return diccionario_de_datos

#%%
precios = leer_precios("..\Data\precios.csv")
camion,headers = leer_camion("..\Data\camion.csv")

#%%
costo = sum([s["cajones"] * s["precio"] for s in camion])
print(costo)
#%%
precios = sum([s["cajones"] * precios[s["nombre"]] for s in camion])
print(precios)
# %%
nombre_cajones = {s["nombre"] : s["cajones"] for s in camion}
nombre_cajones
#%%
import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
#%%
select = ['nombre', 'cajones', 'precio']
#%%
indices = [headers.index(ncolumna) for ncolumna in select]
#%%
row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
record
#%%
row = next(rows)
record = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
record
#%%
types = [ str, int, float]
row = next(rows)
row
#%%
converted = [func(val) for func, val in zip(types, row)]
converted
#%%
converted_dict = [{name:func(val) for name, func, val in zip(headers, types,row)} for row in rows]
converted_dict #no puede convertir string a float, hay un dato vacío
#%%
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
#%%
headers
#%%
row
#%%
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) if "/" not in val else tuple([int(v) for v in val.split("/")]) for func, val in zip(types, row) ]
record = dict(zip(headers, converted))
record
# %%
