#%%
import numpy as np
import random
from matplotlib import pyplot as plt

def crear_album(figus_total):
    return np.zeros(figus_total,dtype = int)

def album_incompleto(A):
    return True if 0 in A else False

def comprar_paquete(figus_total,figus_paquete):
    return [random.randint(0,figus_total-1) for figu in range(figus_paquete)]

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while 0 in album:
        for figurita in comprar_paquete(figus_total,figus_paquete):
            album[figurita] = 1 if album[figurita] == 0 else album[figurita] + 1
        paquetes += 1
    return paquetes

def experimento_paquetes(n_repeticiones,figus_total,figus_paquetes):
    lista_total_paquetes = [cuantos_paquetes(figus_total,figus_paquetes) for _ in range(n_repeticiones)]
    return np.mean(lista_total_paquetes)


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas
#%%

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
