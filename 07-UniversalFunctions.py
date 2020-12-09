# -*- coding: utf-8 -*-

# universal functions (ufunc) operan sobre cada elemento de un ndarray

import numpy as np

x = np.arange(10).reshape(2,-1)

np.sqrt(x)

np.exp(x)

y = np.random.randn(10).reshape(2,-1)

np.maximum(x,y)

residuo, entero = np.modf(x)


# ejemplos de ufunc unarias: 
# abs, fabs, sqrt, square, exp, log, log10, log2, log1p
# sign, ceil, floor, rint, modf, isnan, isfinite, isinf,
# cos, cosh, sin, sinh, tan, tanh
# arccos, arccosh, arcsin, arcsinh, arctan, arctanh
# logical_not

# ufunc binarias:
# add, subtract, multiply, divide, floor_divide, power (**)
# maximum, fmax, minimum, fmin, mod, copysign
# greater, greater_equal, less, less_equal, equal, not_equal
# logical_and (&), logical_or (|), logical_xor (^)

# función que calcula distancia entre puntos:

puntos = np.arange(-2,2,0.1)
xs, ys = np.meshgrid(puntos, puntos)

# JUPYTER
# # crea arreglo z que tenga la distancia al origen de los puntos definidos por xs, ys
# import matplotlib.pyplot as plt
# plt.imshow(z, cmap = plt.cm.gray)
# plt.colorbar()
# plt.title("Distancia al origen de puntos en x, y")
# Text(0.5,1,'calculada como $\sqrt{x^2+y^2}$')


# lógica condicional: en jupyter
#resultado = np.where(condicion, xarr, yarr)  

# Estadística, paso de axis
#arr.mean(), np.mean(arr)
# sum()
# std, var, min, max, argmin, argmax, cumsum, cumprod
# sort

# operaciones de conjuntos:
# unique, intersect1d, union1d, in1d, setdiff1d, setxor1d
