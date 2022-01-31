#%%
import random 

#%%
def tirar():
    tirada = []
    for _ in range(5):
        tirada.append(random.randint(1,6))
    return tirada
#%%
#def es_generala(tirada):
#tirada = tirar()
#%%
#print(tirada)
#%%
def es_generala(tirada):
    if min(tirada) != max(tirada):
        for i in range(3):
            a_tirar_de_nuevo = [tirada.count(i) for i in tirada]
            tirada = [random.randint(1,6)  if i < max(a_tirar_de_nuevo) else tirada[a_tirar_de_nuevo.index(i)] for i in a_tirar_de_nuevo ]
    return min(tirada) == max(tirada) 

def es_generala_servida(tirada):
    return min(tirada) == max(tirada) 
# #%%
N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
G2 = sum([es_generala_servida(tirar()) for i in range(N)])
prob = G/N
prob_servida = G2/N
# #%%
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala común mediante {prob:.6f}.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob_servida:.6f}.')
# #%%W
#corto en "semillas"