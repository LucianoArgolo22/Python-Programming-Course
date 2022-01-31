#%%
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    ''' 
    if hasta > desde:
        acum = 0
        for i in range(desde,hasta):
            acum += i
        return acum
        
    else:
        return 0
