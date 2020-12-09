# -*- coding: utf-8 -*-

import numpy as np

muestras = np.random.normal(size=(4,4))

# semilla con seed global
np.random.seed(1234)

# semilla con entornos aislados

rng = np.random.RandomState(1234)
muestras = rng.randn(8).resize(4,-1)

# funciones de numpy.random
# seed, permutation, shuffle, rand, randint, randn
# binomial, normal, beta, chisquare, gamma, uniform

# caminata aleatoria con Numpy:
npasos = 1000
muestras = np.random.randint(0,2, size=npasos)
pasos = np.where(muestras > 0, 1, -1)
caminata = pasos.cumsum()
import matplotlib.pyplot as plt
plt.plot(caminata[:100])

caminata.min()
caminata.max()

# primer paso en que caminata llega a un valor en particular:
indice_primer_paso = (np.abs(caminata) >=10).argmax()

# Múltiples caminatas a la vez:

# caminata aleatoria con Numpy:
npasos = 1000
ncaminatas = 100
muestras = np.random.randint(0,2, size=(ncaminatas,npasos))
pasos = np.where(muestras > 0, 1, -1)
caminatas = pasos.cumsum(1)
import matplotlib.pyplot as plt
plt.plot(caminatas[0,:100])

caminatas.min()
caminatas.max()

# primer paso en que caminata llega a un valor en particular:
hist10 = (np.abs(caminata) >=10).any(1)

indices_cruce = (np.abs(caminatas[hist10])>=10).argmax(1)

indices_cruce.mean()
    