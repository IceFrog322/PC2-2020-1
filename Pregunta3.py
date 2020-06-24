import numpy as np
m = np.random.randint(0,20, size=(4,3))
print(m)
n = np.delete(m,[1],axis=1)
print(n)
p = m[:,1]
print(p)
matriz = np.append(n,p,axis=1)
print(matriz)
def mueve_col(arreglo,índice):
    m = np.random.randint(0,20, size=(4,3))
    print(m)
    n = np.delete(m,[1],axis=1)
    print(n)
    p = m[:,1]
    print(p)
    matriz = np.append(n,p,axis=1)
    print(matriz)



