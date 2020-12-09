#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 07:54:21 2020

@author: mmorales

NumPy: Logical operators

"""


import numpy as np

a = np.array([1,2,3,4]).reshape(1, -1) # "a" is a row vector
b = np.array([1,3,6]).reshape(-1, 1) # "b" is a column vector
c = (a == b)
print('c:')
print(c)
print('----------')
d = (a * b)
print('d:')
print(d)
print('----------')
e = (a + b)
print('e:')
print(e)
print('----------')
f = (a > b)
print('f:')
print(f)
print('----------')
print(f'c.shape is {c.shape}. d.shape is {d.shape}. e.shape is {e.shape}. f.shape is {f.shape}.')
print('----------')

# Transposición
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)


# Multiplicación de matrices:
# producto punto
punto = np.dot(arr,arr.T)
print(punto)

punto = arr.dot(arr.T)
print(punto)


# Multiplicación de matrices
    
v = np.array([1,2])
A = np.array([[1,2],[3,4]])
prod = v @ A
prod = np.matmul(v,A)

A_diag = np.diag(A)
left_mult = A_diag @ A

left_mult = a.reshape(1,-1) * A

#algunas operaciones mas de algebra lineal
#from numpy, linalg import inv,qr

X=np.random.rand(5,5)
B=X.T@X
IB=np.linalg.inv(B)
B.dot(IB)
q,r=np.linalg.qr(B)





 