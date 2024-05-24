"""Funcion que devuelva el minimo elemento de una matriz MxN"""
"""Funcion que sume todos los elementos de matriz MxN y devuelva resultado"""

def rellenarMatriz(matriz):
    fila=len(matriz)
    columna=len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            n=int(input("Ingrese un numero: "))
            matriz[f][c]=n
    return matriz

def imprimirMatriz(matriz,f=0,c=0):
    if f==len(matriz): #si f que se iba incrementando llega la ultima fila. 
        print()
    else:
        if c<=len(matriz[f])-1: #Para ir imprimiendo las columnas, c tiene que ser menor al largo de la fila.
            print("%3d" %matriz[f][c],end="") #imprimir en tres espacios la fila y la columna
            imprimirMatriz(matriz,f,c+1) #volver a hacer pero la misma fila incrementando columna
        else: #se llegó al final de la columna
            print() #salto de linea
            imprimirMatriz(matriz,f+1,0) #incrementamos la fila, y seteamos la columna en 0 para que arranque de nuevo. 
        
def devolverMinimo(matriz,f=0,c=0,min=0):
    min=matriz[f][c]
    if f == len(matriz):
        print()
    else:
        if c<=len(matriz[f])-1:
            

        else:
            devolverMinimo()
        

fila=3
columna=4
matriz=[[0]*columna for i in range(fila)]
rellenarMatriz(matriz)
imprimirMatriz(matriz)