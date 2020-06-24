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
    print(cadena)

print(crea_arreglo(4,5))





