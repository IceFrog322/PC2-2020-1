#Pregunta2
import random
def crea_arreglo(filas,columnas):

    M = []
    for i in range(filas):
        M.append([0]*columnas)
    
    for i in range(filas):
        for j in range(columnas):
            M[i][j]=random.randint(0,50)
    
    cadena = ""
    for i in range(filas):
        for j in range(columnas):
            cadena=cadena+"\t"+str(M[i][j])
        cadena=cadena+"\n"
    return cadena

print(crea_arreglo(4,5))

#pregunta3

import numpy as np

def mueve_col(arreglo,índice):
    arreglo = np.random.randint(0,20, size=(4,3))
    print(arreglo)
    n = np.delete(arreglo,[índice],axis=1)
    print(n)
    p = arreglo[:,índice]
    print(p)
    matriz = np.append(n,p,axis=1)
    return matriz




