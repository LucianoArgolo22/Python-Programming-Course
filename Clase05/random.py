#%%
import random

from numpy import true_divide 

dado = random.randint(1,6)
#%%
def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada
#%%
def es_generala(tirada):
    return min(tirada) == max(tirada)

#%%
tirada = tirar()
tirada
# %%
print(es_generala(tirada))
#%%
N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
#%%
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#%%
import random
random.seed(0)

tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))

print(tirada)
#%%
#experimento con reposicion
random.choices(tirada,k=3)

