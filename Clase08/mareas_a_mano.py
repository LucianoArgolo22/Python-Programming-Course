#%%
import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')

#%%
df.head()
#%%
df.index
#%%
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

#%%
df.head()

#%%
df['1-18-2014 9:00':'1-18-2014 18:00']

#%%
df.loc['2-19-2014']
#%%
df.loc['12-25-2014':].plot()

#%%
df['10-15-2014':'12-15-2014'].plot()

#%%
dh = df['12-25-2014':].copy()

#%%
delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 15 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()