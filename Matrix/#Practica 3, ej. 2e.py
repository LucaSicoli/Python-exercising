#Practica 3, ej. 2e
def RellenarMatriz():
    n=1
    matriz=[]
    for f in range (4):
        matriz.append([])
        for c in range (4):
            matriz[f].append(0)
            
    for f in range(4):
        for c in range(4):
            if f%2==0:
                if c%2!=0:
                    matriz[f][c]=n
                    n=n+1
            else:
                if c%2==0:
                    matriz[f][c]=n
                    n=n+1
    return matriz   

def MostrarMatriz(m):
    fila=len(m)
    columna=len(m[0])
    for f in range(fila):
        for c in range(columna):
            print("%3d"%m[f][c], end="")
        print()
        
m=RellenarMatriz()
MostrarMatriz(m)
