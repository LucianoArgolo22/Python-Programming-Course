#%%
import numpy as np
from matplotlib import pyplot as plt
#%%
temperaturas = np.load(r"..\Data\temperaturas.npy")
#%%
plt.hist(temperaturas,bins=20)
plt.show() 