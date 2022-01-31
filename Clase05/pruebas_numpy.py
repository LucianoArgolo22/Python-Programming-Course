#%%
import numpy as np
#%%
a = np.array([1,2,3,4,5])
# %%
a = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
#%%
a[2,3]
# %%
b = np.arange(1,20,2)
b
#%%
c = np.linspace(1,19,num=10,dtype=int)
c

#%%
np.ones(3, dtype= int)
#%%
arr = np.array([7,3,2,4,6,7],dtype=int)
# %%
np.sort(arr)
#%%
np.concatenate((c,arr))
#%%
#cambiando la forma en que los concateno
arra2 = np.concatenate((c.reshape(2,5),arr.reshape(2,3)),axis = 1)

#%%
arra2.shape
#%%
arra2.ndim
#%%
arra2.size
#%%
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
#(6,)
#%%
vec_fila = a[np.newaxis, :]
vec_fila.shape
#(1, 6)
#%%
vec_col = a[:, np.newaxis]
vec_col.shape
#(6, 1)
#%%
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
#[1 2 3 4]
#%%
five_up = (a >= 5)
five_up
#%%
print(a[five_up])
#[ 5  6  7  8  9 10 11 12]
#%%
pares = a[a%2==0]
print(pares)
#[ 2  4  6  8 10 12]
#%%
#Ya sea para seleccionar elementos directamente:

c = a[(a > 2) & (a < 11)]
print(c)
#[ 3  4  5  6  7  8  9 10]
#o para definir una nueva variable booleana:

five_up = (a > 5) | (a == 5)
print(five_up)
"""[[False False False False]
 [ True  True  True  True]
 [ True  True  True True]]
"""
# %%
#Si tenés la matriz:

b = np.array([[1, 1], [2, 2]])
#podés sumar los datos de cada columna con:

b.sum(axis=0)
#array([3, 3])

#y los datos de cada fila usando:
b.sum(axis=1)
#array([2, 4])

#%%
data.max()
#2.0
data.min()
#1.0
data.sum()
#3.0
#%%
np.save('filename', a)

#%%
b = np.load('filename.npy')
#%%
csv_arr = np.array([9,9,8,72,2,34,5])
csv_arr
#%%
np.savetxt('new_file.csv', csv_arr)
#%%
np.loadtxt('new_file.csv')


