import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)    
    return pasos.cumsum()

def caminata_mas_alejada(caminatas):
    caminata_alejada = []
    for caminata in caminatas:
        distancia = max(abs(caminata))
        caminata_alejada.append(distancia)
    return caminatas[caminata_alejada.index(max(caminata_alejada))]



def caminata_menos_alejada(caminatas):
    caminatas_puntaje = []
    for caminata in caminatas:
        acum = 0
        for distancia in caminata:
            acum += distancia
        caminatas_puntaje.append(abs(acum))
    return caminatas[caminatas_puntaje.index(min(caminatas_puntaje))]
    


N = 100000

caminatas = []
fig = plt.figure()
plt.subplot(2, 1, 1)
for i in range(12):
    caminata = randomwalk(N)
    plt.plot(caminata)
    caminatas.append(caminata)
print(sum(caminatas))
plt.title("12 Caminatas al azar")
plt.xticks([])
plt.ylim(-500.0, 500.0)


plt.subplot(2,2,3)
plt.title("Camino más alejado")
plt.plot(caminata_mas_alejada(caminatas))
plt.xticks([])
plt.ylim(-500.0, 500.0)

plt.subplot(2,2,4)
plt.title("Camino menos alejado")
plt.plot(caminata_menos_alejada(caminatas))
plt.xticks([])
plt.ylim(-500.0, 500.0)
plt.show()

# %%
