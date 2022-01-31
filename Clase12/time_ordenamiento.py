#%%
import random
import matplotlib.pyplot as plt
import numpy as np
import time as tt

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    lista2 = lista.copy()
    comp = 0
    comp_total = 0
    for i in range(len(lista2) - 1):
        if lista2[i + 1] < lista2[i]:
            comp = reubicar(lista2, i + 1)
        #print("DEBUG: ", lista2)
        comp_total = comp_total + comp
    return comp_total


def merge(lista3, lista4):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones = 0
    while(i < len(lista3) and j < len(lista4)):
        comparaciones +=1
        if (lista3[i] < lista4[j]):
            resultado.append(lista3[i])
            i += 1
        else:
            resultado.append(lista4[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista3[i:]
    resultado += lista4[j:]
    return resultado, comparaciones

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])[0]
        der = merge_sort(lista[medio:])[0]
        lista_nueva = merge(izq, der)[0]
        comparaciones = merge(izq, der)[1] + comparaciones
    return lista_nueva, comparaciones

    
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    lista3 = lista.copy()
    n = len(lista3) - 1
    comp_total = 0

    while n > 0:
        p, comp = max(lista3, 0, n)
        comp_total = comp_total + comp

        lista3[p], lista3[n] = lista3[n], lista3[p]
        #print("DEBUG: ", p, n, lista3)

        # reducir el segmento en 1
        n = n - 1
    return comp_total

def reubicar(lista2, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista2[p]
    comp = 0
    j = p
    while j > 0 and v < lista2[j - 1]:
        lista2[j] = lista2[j - 1]
        j -= 1
        comp = comp + 1
    comp = comp + 1
    lista2[j] = v
    return comp


def max(lista, c, b):
    acum = 0
    posicion_max = c
    for i in range(c + 1, b + 1):
        if lista[i] > lista[posicion_max]:
            posicion_max = i
        acum = acum + 1
    return posicion_max, acum

def ord_burbujeo(list):
    hubo_cambio = True
    while(hubo_cambio):
        #corto la secuencia si no hay nada que cambiar, o sea que ya está ordenado
        hubo_cambio = False
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                # Swap
                list[i], list[i+1] = list[i+1], list[i]
                hubo_cambio = True
        
global lista

def valores_random(x):
    lista = random.sample(range(1000),x)
    return lista

largos = np.arange(200)
lista_merge = np.zeros(200)
lista_insercion = np.zeros(200)
lista_burbujeo = np.zeros(200)
lista_seleccion = np.zeros(200)

for x in largos:
    lista=valores_random(x)
    lista_merge[x]=merge_sort(lista)[1]
    lista_insercion[x]=ord_insercion(lista)
    lista_burbujeo[x]=ord_burbujeo(lista)
    lista_seleccion[x]=ord_seleccion(lista)

for i,lista in enumerate(lista):
    lista_seleccion[i]=tiempo_seleccion
    tiempo_seleccion = tt.timeit('ord_seleccion(lista)', number = 10,globals = globals())
    tiempo_insercion = tt.timeit('ord_insercion(lista)', number = 10,globals = globals())
    lista_insercion[i]=tiempo_insercion
    tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = 10,globals = globals())
    lista_merge[i]=tiempo_merge
    tiempo_burbujeo = tt.timeit('ord_burbujeo(lista)', number = 10,globals = globals())
    lista_burbujeo[i]=tiempo_burbujeo

plt.plot(largos,lista_merge)
plt.plot(largos,lista_insercion)
plt.plot(largos,lista_burbujeo)
plt.plot(largos,lista_seleccion)
plt.ylabel("Comparaciones")
plt.xlabel("Longitud")
plt.legend(["Lista Merge","Lista Insercion","Lista Burbujeo","Lista Seleccion"])
plt.show()


