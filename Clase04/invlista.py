#%%
def invertir_lista(lista):
    invertida = []
    print(len(lista))
    for e in range(len(lista)-1,-1,-1): # Recorro la lista
        invertida.append(lista[e]) #agrego el elemento e al principio de la lista invertida
    return invertida

#con invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
#devuelve
#['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']


# con invertir_lista([1, 2, 3, 4, 5])
#devuelve
#[5, 4, 3, 2, 1]

#%%
invertir_lista([0, 0, -1, 0, 0, 0, 1, 1, 1, 1, 1, 1])
