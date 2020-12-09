# -*- coding: utf-8 -*-

import numpy as np

import pandas as pd

from pandas import Series, DataFrame

#%% Series

# similares a un diccionario ordenado de longitud fija

obj = pd.Series([4,7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)

# objetos con índices específicos
obj = pd.Series([4,7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj)
print(obj.values)
print(obj.index)

# Funciones de NumPy y operaciones tipo NumPy
print(obj[obj > 0])

print(obj * 2)

print(np.exp(obj))

# Creación con pd.Series a partir de diccionarios

#%% DataFrames

# tabla rectangular (2 dimensiones) que contiene 
# una colección ordenada de columnas
# cada columna puede tener un tipo diferente
# tiene índices para renglón y para columna
# dict de Series que comparten el mismo índice

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print(frame)

print(frame.head()) #solo muestra los primeros 5 renglones

print(frame['state']) # recupera la columna como Series

# se pueden crear a partir de 
# ndarray de 2D de NumPy
# diccionario de array, listas, o tuplas
# arreglo de registros o estructuras de NumPy
# dict de Series
# dict de dicts
# Arreglo 

#%% Reindex

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                      index=['a', 'c', 'd'],
                      columns=['Ohio', 'Texas', 'California'])

print(frame)

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

frame.loc[['a', 'b', 'c', 'd'], states]


#%% ignorar valores de un Axis en Series

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
obj.drop(['d', 'c'])

#%% lo mismo en DataFrame

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])

data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1)

# Selección con loc usando nombres de renglones y columnas
data.loc['Colorado', ['two', 'three']]

# misma seleccón con índices enteros
data.iloc[2, [3, 0, 1]]

# usando slices
data.loc[:'Utah', 'two']
data.iloc[:, :3][data.three > 5]