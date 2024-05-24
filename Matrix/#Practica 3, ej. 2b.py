def RellenarMatriz():
    n=3
    matriz=[]
    for f in range (4):
        matriz.append([])
        for c in range (4):
            matriz[f].append(0)
            
    for f in range(4):
        for c in range(4):
            if f + c == 4-1:
                matriz[f][c]=3**n
                n=n-1
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