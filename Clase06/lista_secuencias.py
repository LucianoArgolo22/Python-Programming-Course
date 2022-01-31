#%%
def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    
    print(s)
    return s


def listar_secuencias(n):
    lista_binaria = [0]*n
    listas_binarias = []
    for _ in range(n):
        lista_binaria = incrementar(lista_binaria)
        listas_binarias.append(lista_binaria)

    return listas_binarias

