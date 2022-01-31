#%%
#Arbolado
import pandas  as pd
import seaborn as sns

#%% ---------------------
df_parque = pd.read_csv(r"..\Data\arbolado.csv",",")
cols_sel_parque = ['nombre_cie', 'diametro', 'altura_tot']

df_vereda = pd.read_csv(r"..\Data\arbolado-publico-lineal-2017-2018.csv",",")
cols_sel_vereda = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']

# %%
df_parque = df_parque[cols_sel_parque]

df_vereda = df_vereda[cols_sel_vereda]

# %%
#Tipuana Tipu
df_tipas_parques = df_parque[df_parque["nombre_cie"].isin(["Tipuana Tipu"])].copy()
df_tipas_veredas = df_vereda[df_vereda["nombre_cientifico"].isin(["Tipuana tipu"])].copy()
#%%
df_tipas_veredas = df_tipas_veredas.rename(columns = {"diametro_altura_pecho":"diametro","altura_arbol":"altura_tot","nombre_cientifico":"nombre_cie"})
df_tipas_veredas.columns
#%%
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
#%%
df_tipas.boxplot('diametro', by = 'nombre_cie')
#%%
df_tipas.boxplot('altura_tot', by = 'nombre_cie')
#%%
sns.pairplot(data = df_tipas[cols_sel_parque], hue = 'nombre_cie')
