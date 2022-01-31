#%%
import csv
def leer_parque(archivo,parque):
    f = open(archivo, encoding = "UTF-8")
    rows = csv.reader(f)
    headers = next(rows)
    lista_arboles = []
    for fila in rows:
        pares = dict(zip(headers,fila))
        if pares["espacio_ve"] == parque:
            lista_arboles.append(pares)
    return lista_arboles

def especies(lista_arboles):
    lista_especies = []
    for arboles in lista_arboles:
        lista_especies.append(arboles["nombre_com"])
    return set(lista_especies)

def leer_arboles(archivo):
    f = open(archivo, encoding = "UTF-8")
    rows = csv.reader(f)
    headers = next(rows)
    lista_arboles=[{ nombre: val for nombre,val in zip(headers,row)} for row in rows]
    return lista_arboles


def medidas_de_especies(especies,arboleda):
    arboleda = leer_arboles(arboleda)
    arbolado = [{arbol["nombre_com"] : (float(arbol['altura_tot']),float(arbol["diametro"]))} for arbol in arboleda if arbol["nombre_com"] in especies]
    return arbolado
#%%
arboleda = leer_arboles(r"..\Data\arbolado.csv")
arboleda
#%%
H = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
#%%
Alt_Diam = [(float(arbol['altura_tot']),arbol["diametro"]) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
Alt_Diam
#%%
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
list_Dict_Alt_Diam = [{arbol["nombre_com"] : (float(arbol['altura_tot']),float(arbol["diametro"]))} for arbol in arboleda if arbol["nombre_com"] in especies]
list_Dict_Alt_Diam
#%%
especies = ['Jacarandá']
lista = medidas_de_especies(especies,r"..\Data\arbolado.csv")
# %%
len(lista)

