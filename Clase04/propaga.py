#%%
#Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo propaga.py.
def invertir_lista(lista):
    invertida = []
    for e in range(len(lista)-1,-1,-1): # Recorro la lista
        invertida.append(lista[e]) #agrego el elemento e al principio de la lista invertida
    return invertida

def recorrerLista(lista):
    for i in range(len(lista)):
        try:
            if lista[i] == 1 and lista[i+1] == 0:
                lista[i+1] = 1

        except :
            
            try:
                if lista[i]  == 1 and lista[i+1] == 0:
                    lista[i+1] = 1
            
            except:
                if lista[i]  == 1 and lista[i-1] == 0:
                    lista[i-1] = 1
 
    return lista

def propagar(lista):
    lista = recorrerLista(lista) #recorro lista hacia adelante
    lista = invertir_lista(lista) #invierto lista
    lista = recorrerLista(lista) #recorro lista hacia adelante (al revés ahora)
    lista = invertir_lista(lista) #invierto
    return lista

#lista_de_prueba1 = [0,0,1,0,-1,0,0,-1,0,0,0,1,0,-1,0,0,0]
#propagar(lista_de_prueba1)
#devuelve [1, 1, 1, 1, -1, 0, -1, 1, 1, 1, 1, 1, -1, 0, 0, 0]