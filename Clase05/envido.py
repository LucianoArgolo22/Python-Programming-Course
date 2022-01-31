#%%
import random


def mano_truco():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    return random.sample(naipes,k=3)


def proba_envido():
    tirada = mano_truco()
    tirada = [(0,i[1]) if i[0] in [10,11,12] else (i[0],i[1]) for i in tirada ]
    if tirada[1][1] == tirada[0][1] and (tirada[1][0] + tirada[0][0] + 20) > 30 :
        return True
    elif tirada[1][1] == tirada[2][1] and (tirada[1][0] + tirada[2][0] + 20) > 30 :
        return True
    elif tirada[0][1] == tirada[2][1] and (tirada[0][0] + tirada[2][0] + 20) > 30 :
        return True
    else:
        return False

#%%

N = 100000
G = sum([proba_envido() for i in range(N)])
prob = G/N
print(prob)

#la probabilidad es de alrededor 6.159%
