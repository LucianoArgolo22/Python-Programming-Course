#%%
import numpy as np
import random

def crear_album(figus_total):
    return np.zeros(figus_total,dtype = int)

def album_incompleto(A):
    return True if 0 in A else False


def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    figus = 0
    while 0 in album:
        figurita = comprar_figu(figus_total)
        album[figurita] = 1 if album[figurita] == 0 else album[figurita] + 1
        figus += 1
    return figus

# %%
def experimento_figus(n_repeticiones,figus_total):
    lista_total_figus = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    return np.mean(lista_total_figus)
#%%
experimento_figus(100,670)
# %%
