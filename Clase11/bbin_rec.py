#%%
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