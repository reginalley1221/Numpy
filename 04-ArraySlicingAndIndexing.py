# -*- coding: utf-8 -*-

import numpy as np

# https://numpy.org/doc/stable/reference/arrays.indexing.html

# i:j:k
#   i: start
#   j: stop
#   k: step

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x[1:7:2]
print(x)
#array([1, 3, 5])

# i,j negativos: n+1 y n+j, donde n es el número de elementos en la dimensión correspondiente
# k negativo: avanca en reversa

y = x[-2:10]
print(y)
#array([8, 9])

y = x[-3:3:-1]
print(y)
#array([7, 6, 5, 4])


# i,j,k defaults cuando faltan en descripción de slices
# faltante i: 0 para k>0, n-1 para k<0
# faltante j: n para k>0, n-1 para k<0
# faltante k: 1

y = x[5:]
print(y)
#array([5, 6, 7, 8, 9])

# default para dimensiones no especificadas. :
    
x = np.array([[[1],[2],[3]], [[4],[5],[6]]])
print(x.shape)
#(2, 3, 1)
y = x[1:2]
print(y)
# array([[[4],
#         [5],
#         [6]]])

# Ejemplos mas completos:

    
# Selecciona los 5 elementos de mayor valor
np.random.seed(1)
y = np.arange(100)
np.random.shuffle(y)  # barajear 

mayores = np.sort(y)[-5:]

# Varias operaciones sobre arreglo:
raw_data = [[5.3, 3.1, 1, 7, 8.3], [3, 5, 6.3, 4, 45], [99, 1, 101.2, 2., 0.2],[0., 0, 1., 22, 44.]]
data = np.array(raw_data).astype(np.float32)
print(type(data)) 
print(data.dtype) 
print(data)

# Duplicar los valores de renglones pares
data[::2, :] *= 2 
print(data)

# asociación de datos entre arreglos
estados = np.array(['Guerrero', 'Morelos', 'Veracruz', 'México', 'Guerrero', 'Morelos', 'Jalisco'])
datos = np.random.randn(7, 4)

estados == 'Guerrero'
datos[estados == 'Guerrero']


# revertir secuencia en columnas nones
data[:, 1::2] = data[:, 1::2][::-1, :]
print(data) # notar el cambio de órden en dos columnas



# agregar un eje
print(data.shape)
data_shape_expand_none = data[None] 
data_shape_expand_newaxis = data[np.newaxis] 
print(data_shape_expand_none.shape) 
print(data_shape_expand_newaxis.shape)

#  this can work for adding a new axis along any dimension.
print(data.shape)
data_shape_expand_none = data[:, None] 
data_shape_expand_newaxis = data[:, np.newaxis] 
print(data_shape_expand_none.shape) 
print(data_shape_expand_newaxis.shape)

# permutar
