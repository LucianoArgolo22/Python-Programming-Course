#%%
import csv
import numpy as np
from matplotlib import pyplot as plt

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
    arbolado = [{arbol["nombre_com"] : (float(arbol['altura_tot']), float(arbol["diametro"]))} for arbol in arboleda if arbol["nombre_com"] in especies]
    return arbolado

#def medidas_de_especies(especies,arboleda):
#    arboleda = leer_arboles(arboleda)
#    arbolado = [{"nombre": arbol["nombre_com"], "altura_tot": float(arbol['altura_tot']),"diametro": float(arbol["diametro"])} for arbol in arboleda if arbol["nombre_com"] in especies]
#    return arbolado

def scatter_hd(lista_de_pares):
    H = np.array([list(i.values())[0][0] for i in arbolado])
    D = np.array([list(i.values())[0][1] for i in arbolado])
    plt.scatter(H,D,s = 10, c="green", alpha=0.5)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto")
#%%
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
arbolado = medidas_de_especies(especies,r"..\Data\arbolado.csv")

scatter_hd(arbolado)


