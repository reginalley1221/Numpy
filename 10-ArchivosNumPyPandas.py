# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#%%  NumPy

arr = np.arange(10)
np.save('some_array', arr)

arr2 = np.load('some_array.npy')

# múltiples arreglos
np.savez('array_archive.npz', a=arr, b=arr2)
arch = np.load('array_archive.npz')
arch['b']

# multiples arreglos comprimidos:
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)

#%% Pandas

df = pd.read_csv('10-ejemplo.csv')

df = pd.read_csv('10-ejemplo_sinheaders.csv', header=None) # si no tiene header

names=['a', 'b', 'c', 'd', 'message']
df = pd.read_csv('10-ejemplo_sinheaders.csv', names=names)

# definiendo una columna como índice
df = pd.read_csv('10-ejemplo_sinheaders.csv', names=names, index_col='message')

df.to_csv('10-salida.csv')