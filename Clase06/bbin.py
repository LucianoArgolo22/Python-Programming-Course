
def busqueda_lineal_ordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        elif z > e:
            break
    return pos

#%%
"""
Como ejemplo si se usan 1 millon de casos:
1-El algoritmo de búsqueda lineal hará, en el peor caso,
 un millón de comparaciones. Este caso se da si el elemento buscado no
  está en la lista o está en la última posición. Como se ve la cantidad
   de operaciones es proporcional al largo de la lista. Si el elemento
    buscado está en la lista el algoritmo realizará, en promedio
    , 500,000 comparaciones.
2-El algoritmo de búsqueda binaria hará como máximo log2(1,000,000)
 comparaciones, o sea ¡no más que 20 comparaciones!."""


def donde_insertar(lista, x, verbose = True):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    encontrado = ""
    while izq <= der:
        medio = (izq + der) // 2

        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            encontrado = "si"
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if not encontrado:    
        if x > lista[medio]:
            #lista.insert(medio + 1,x)
            return print(f' El elemento se puede insertar en la posicion { medio + 1 }')
        elif x < lista[medio]:
            return print(f' El elemento se puede insertar en la posicion { medio }')
            #lista.insert(medio ,x)

def insertar(lista, x):
    izq = 0
    der = len(lista) - 1
    encontrado = ""
    while izq <= der:
        medio = (izq + der) // 2

        if lista[medio] == x:
            encontrado = "si"
            return medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if not encontrado:    
        if x > lista[medio]:
            lista.insert(medio + 1, x)
            return medio + 1
        elif x < lista[medio]:
            lista.insert(medio, x)
            return medio

