#Ej. 1 practica 3
def cargarMatriz(num):
    matriz=[]
    for f in range(num):
        matriz.append([])
        for c in range (num):
            n=int(input("ingrese un numero: "))
            matriz[f].append(n)
    return matriz

def imprimirMatriz(mat):
    for f in range (len(mat)):
        for c in range(len(mat[0])):
            print("%3d"%mat[f][c], end="")
        print()
    
def diagonalSimP(mat): #punto H
    flag=0
    for f in range(len(mat)):
        for c in range (len(mat[0])):
            if  mat[f][c] != mat[c][f]:
                flag=1
    if flag==1:
        print ("No es simétrica con respecto a su diagonal principal")
    else:
        print("Es simétrica con respecto a su diagonal principal")

def diagonalSimS(mat): #punto J :)
    sim=True
    for i in range (len(mat)-1):
        for j in range (len(mat)-1-i):
            if mat[i][j]!=mat[len(mat)-1-j][len(mat)-1-i]:
                sim=False
    if sim==False:
        print ("No es simétrica con respecto a su diagonal secundaria")
    else:
        print("Es simétrica con respecto a su diagonal secundaria")
        
#prograPrinc
numero=int(input("ingrese el tamaño de la matriz"))
mat=cargarMatriz(numero)
imprimirMatriz(mat)
diagonalSimP(mat)
diagonalSimS(mat)
