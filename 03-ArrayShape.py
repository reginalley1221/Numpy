#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:32:49 2020

@author: mmorales
"""

import numpy as np

a = np.arange(6) #es como el range de la biblioteca standard
print("a: ", a)

b = np.arange(12).reshape(4,3)
print("b: \n",b)

c = np.arange(24).reshape(2,3,4) #dos elementos de 3x4
print("c with reshape(2,3,4): \n", c)
print("c's shape is: ", c.shape)

c = c.reshape(3,2,4) #tres elementos de 2x4
print("c after reshape(3,2,4): \n", c)
print("c's shape is: ", c.shape)

c = c.reshape(3,-1,4)
print("c after reshape(3,-1,4): \n", c)
print("c's shape is: ", c.shape)

c = c.reshape(3,-1)
print("c after reshape(3,-1): \n", c)
print("c's shape is: ", c.shape)

c = c.reshape(-1,3)
print("c after reshape(-1,3): \n", c)
print("c's shape is: ", c.shape)

c = c.reshape(-1)
print("c after reshape(-1): \n", c)
print("c's shape is: ", c.shape)

c = c.reshape(-1,1)
print("c after reshape(-1,1): \n", c)
print("c's shape is: ", c.shape)


print("a few tests of copying by value or by references:")

print("first use numpy")
d = np.zeros((2,2))
e = d
d[0,0] = 2
print("d: ", d)
print("e: ", e)

print("now using python lists")
f = [0,0]
g = f
f[1] = 2
print("f: ", f)
print("g: ", g)

print("now with scalars")
h = 0
i = h
h = 2
print("h: ", h)
print("i: ", i)

