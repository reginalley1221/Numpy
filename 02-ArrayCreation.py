import numpy as np

a = np.array([2,3,4])
print(a)
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)

#a = np.array(1,2,3,4) # ERROR: arguments are not a single sequence (list or tuple)

a = np.array([1,2,3,4]) # This should fix the previous error

# previous arrays were one-dimensional

# two-dimensional array. pass sequence of sequences
b = np.array([(1.5,2,3),(4,5,6)])
print(b)
print(b.dtype)

# specific definition of type of array at creation time
c = np.array([[1,2],[3,4]], dtype=complex)
print(c)
print(c.dtype)

# If size is known in advance, it can be initialized with placeholder contents (growing it later can be expensive)
a = np.zeros((3,4))
print(a)

b = np.ones((2,3,4), dtype=np.int16)
print(b)

c = np.empty((2,3))
print(c)

d = np.arange(10,30,7)
print(d)

from numpy import pi
e = np.linspace(0,2,9)
print(e)

x = np.linspace(0, 2*pi, 100)
print(x)
f = np.sin(x)
print(f)
