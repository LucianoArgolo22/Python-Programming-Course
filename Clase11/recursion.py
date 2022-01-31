#%%
#Recursividad

def sumar(lista):

    if len(lista) == 0:
        return 0
    
    a = sumar(lista[1:])


def sumar(lista):
   """Precondición: len(lista) >= 1.
      Devuelve: La suma de los elementos en la lista."""
   return lista[0] + sumar2(lista[1:])

#%%
def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   res = 0
   if len(lista) != 0:
       print(f"Suma: {sumar(lista[1:])} Lista[0]: {lista[0]} ")
       res = lista[0] + sumar(lista[1:])
       print(f"Resultado: {res}")
   return res

sumar([1,2,3,4,5])

#%%

def promediar_aux(lista):
    suma = lista[0]
    cantidad = 1    
    if len(lista) > 1:
        suma_resto, cantidad_resto = promediar_aux(lista[1:])
        suma += suma_resto
        cantidad += cantidad_resto
    return suma, cantidad


#%%
def promediar(lista):
    """Devuelve el promedio de los elementos de una lista de números."""

    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad

    suma, cantidad = promediar_aux(lista)
    return suma / cantidad

#%%
def triangular(n):
    num = 0
    if n != 0:
        num = n + triangular(n-1)
    return num

triangular(3)

#%%
def cant_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + cant_digitos(n/10)
cant_digitos(1000)
#%%

def posiciones_de(a,b, posiciones = None):
    contador = 0
    if len(posiciones) == None:
        posiciones = []
    if len(a) <= len(b):
        if b in a:
            posiciones.append(a.index(b))
            return contador
        ##posiciones.append(a.index(b))
    else:
        if b in a:
            #posiciones = posiciones + posiciones_de(a[1:],b)
            contador += 1
            posiciones.append(a.index(b))
            return posiciones_de(a[1:],b,posiciones)
        else:
            posiciones_de(a[1:],b,posiciones)

posiciones_de('e e e e', 'e') 

#%%
def maximo(lista):
    max = lista[0]
    if len(lista) == 1:
        return max if max > lista[0] else lista[0]

    else:
        return max if (max > maximo(lista[1:])) else maximo(lista[1:])

maximo([9, 1, 3, 8, 3, 3, 7, 7])




#%%

def digit(n):
    if n < 10:
        return 1
    else:
        return 1 + digit(n/10)

digit(1000)


#%%
def pascal(n,k, result=None):
    if result is None:  # create a new result if no intermediate was given
        result = []
    if len(str(list(range(n)))) == 1:
        return 1
    else:
        result.append(n)
        return 1 + pascal(n-1,k)

pascal(2,1)

#%%
def replicate_recur(times, data, result=None):
    if result is None:  # create a new result if no intermediate was given
        result = []
    if times == 1:
        result.append(data)
    else:
        result.append(data)
        replicate_recur(times - 1, data, result)  # also pass in the "result"
    return result

replicate_recur(5,3)

#%%
#---------larenga.py
def pascal(n,k):
    def pascal_aux(n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        else:
            new_row = [1]
            last_row = pascal_aux(n-1)
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += [1]
        return new_row
    return pascal_aux(n+1)[k]

pascal(5,2)

#%%
#-----------bbin_rec
def bbinaria_rec(lista, e):
    lista = sorted(lista)
    if len(lista) == 0:
        res = False

    elif len(lista) == 1:
        res = lista[0] == e

    else:
        medio = len(lista)//2
        if e == lista[medio]:
            return True

        elif e < lista[medio]:
                return bbinaria_rec(lista[:medio],e)
        
        else:
                return bbinaria_rec(lista[medio:],e)

    return res

bbinaria_rec([1,6,2,2,3,4,5,1],0)


#%%
def pascal_aux(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = pascal_aux(n-1)
        print(last_row)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        print(new_row)
    return new_row

pascal_aux(3)
#%%
def replicar(n,b):
    if b == 0:
        return []
    if len(n) == 1:
        return n * b
    else:
        nueva_fila = [n[0]] * b
        nueva_fila += replicar(n[1:],b)
    return nueva_fila

replicar([1,2,3,4],3)

#%%
#-------hojas_ISO
def medidas_hojas_A(N):
    if N == 0:
        return [(841,1189)]
    else:
        hoja = medidas_hojas_A(N-1)
        hoja += [(int(hoja[-1][1]/2),hoja[-1][0])]
    return hoja

medidas_hojas_A(10)
#%%
prueba = (841,1189)
lista = []
lista.append(prueba)
for i in range(4):
    prueba = (int(prueba[1]/2),prueba[0])
    lista.append(prueba)

lista
#%%
