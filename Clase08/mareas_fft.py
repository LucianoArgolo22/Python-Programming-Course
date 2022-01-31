#%%
from scipy import signal # para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
#%%
inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

#%%
def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran
#%%
freq_sf, fft_sf = calcular_fft(alturas_sf)
#%%
plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")    
plt.ylabel("Potencia (energía)")
plt.show()


# %%
print(signal.find_peaks(np.abs(fft_sf), prominence = 8))