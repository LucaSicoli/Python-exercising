#MATRIZ EN ZIG ZAG
def rellenarmatriz1(mat):
    # Alternativa 1: Rellenando la matriz elemento por elemento.5
    n = len(mat)
    contador = 1
    for f in range(n):
        # Determinamos si la fila es par o impar para definir si se
        # rellena de izquierda a derecha o de derecha a izquierda
        if f%2==0:
            inicio = 0
            fin = n
            incremento = 1
        else:
            inicio = n-1
            fin = -1
            incremento = -1
        for c in range(inicio, fin, incremento):
            mat[f][c] = contador
            contador = contador + 1
def imprimirmatriz(mat):
    for fila in mat:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()
    print("-"*(len(mat)*3+1))  # Línea separadora proporcional al tamaño de la matriz

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
print()
matriz1 = [[0] * n for i in range(n)]
rellenarmatriz1(matriz1)
imprimirmatriz(matriz1)