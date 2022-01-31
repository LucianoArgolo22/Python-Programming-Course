#%%
def buscar_u_elemento(lista, e):
    pos = -1  
    for i, j in enumerate(lista):
        if j == e:   
            pos = i  
            break    
    return pos

def buscar_n_elemento(lista, e):
    pos = -1  
    contador = 1
    for i, j in enumerate(lista):
        if j == e:    
            contador += 1 
            break    
    return contador

def maximo(lista):
    m = lista.pop(0)  #saco el primer elemento de la lista
    #asi no supongo un valor 0, dado que el mismo podria ser máximo de mi conjunto
    for e in lista:  #recorro la lista con los valres generados arriba
        m = m if m > e else e
    return m

def minimo(lista):
    m = lista.pop(0)  #saco el primer elemento de la lista
    #asi no supongo un valor 0, dado que el mismo podria ser máximo de mi conjunto
    for e in lista:  
        m = m if m < e else e #recorro la lista con los valres generados arriba
    return m

#%%


