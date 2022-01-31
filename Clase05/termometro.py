#%%
import random
import numpy as np

#%%
def medir_temp(n):
    lista_temp = []
    for i in range(n):
        lista_temp.append( 37.5 + random.normalvariate(0,0.2))
    
    np.save(r'..\Data\temperaturas', lista_temp)
    
    return lista_temp

#%%
def resumen_temp(n):
    lista_temp = sorted(medir_temp(n))
    val_min = min(lista_temp)
    val_max = max(lista_temp)
    val_mean = sum(lista_temp)/len(lista_temp)
    val_median = lista_temp[int(len(lista_temp)/2)]
    return (val_max,val_min,val_mean,val_median)
#%%
lista_temp = medir_temp(999)
