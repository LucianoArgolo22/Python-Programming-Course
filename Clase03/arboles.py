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


#%%
if __name__ == "__main__":

    try:

        lista_arboles = leer_parque(r"..\Data\arbolado-en-espacios-verdes.csv", 
        "GENERAL PAZ")
        print("Longitud de lista con Parques 'General Paz'",len(lista_arboles))
        arbolitos = especies(lista_arboles)
        print("\n\nLista de Arbolitos: ",arbolitos)
    except:
        Exception