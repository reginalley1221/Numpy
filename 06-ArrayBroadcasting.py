# -*- coding: utf-8 -*-

# concepto de broadcasting



# Escribir funciones
def comparacion(valores, umbral):
    '''

    Parameters
    ----------
    valores : Numpy array shape (1,N)
    umbral : Numpy array shape (M,1)

    Returns
    -------
    res : Numpy array shape (M,N)
        res[i,j] = True si valores[i] >= umbral[j]

    '''
    ftr = valores.reshape(1,-1)
    res = (ftr >= umbral)
    print('valores: ', ftr)
    print('----------')
    print('umbral: ', umbral)
    print('----------')
    print('resultado: ', res)
    print('----------')

    return res

def precision(estimacion, valor_real, umbral):
    '''
    Parameters
    ----------
    estimacion : Numpy array shape (1,N)
    valor_real : Numpy array shape (1,N)
    umbral : escalar

    Returns
    -------
    prec : TYPE
        DESCRIPTION.

    '''
    
    pred = comparacion(estimacion, umbral)
    lbl = valor_real.reshape(1,-1)
    cmp = (pred == lbl)
    prec = cmp.mean(axis=1) # mean over columns
    #para promedio de las rows es axis=0

    print('valor real: ', lbl)
    print('----------')
    print('comparación: ', cmp)
    print('----------')
    print('precisión: ', prec)
    print('----------')

    
    return prec

print('==========')
out = comparacion(np.array([150.,130.,110.]).reshape(1,-1),120)
print('==========')
out = comparacion(np.array([150.,100.,110.,125.]).reshape(1,-1),
                  np.array([120.,130.]).reshape(-1,1))
print('==========')
acc = precision(np.array([150.,100.,110.,125.]).reshape(1,-1),
                 np.array([True,True,False,False]).reshape(1,-1),
                 np.array([120.,130.]).reshape(-1,1))
print('==========')

print('==========')
acc = precision(np.array([150.,100.,110.,125.]).reshape(1,-1),
                 np.array([True,False,False,True]).reshape(1,-1),
                 np.arange(100,120).reshape(-1,1))
print('==========')


