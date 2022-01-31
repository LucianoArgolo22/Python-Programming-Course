#%%
import random
import collections
#%%
def cumpleanito():
    return [random.randint(1,366) for _ in range(30)]
#%%

def proba_cumple():
    cumples = cumpleanito()
    #return [True if tirada.count(cumple) >= 2 else False for cumple in tirada ]
    acumulador = 0
    for cumple in collections.Counter(cumples).items():
        acumulador += 1 if cumple[1] >= 2 else 0
    return acumulador
#%%
proba_cumple()
#%% sigue estando mal
N = 1000
G = sum([proba_cumple() for i in range(N)])
prob = G/N
prob
#%%
lista_cumples = cumpleanito()
collections.Counter(lista_cumples)

