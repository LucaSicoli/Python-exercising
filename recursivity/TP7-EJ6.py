"""La funcion Ackermann A(m,n) se define así: 
    n+1                 si m=0
    A(m-1,1)            si n = 0
    A(m-1,A(m,n-1))     de otro modo 
Imprimir un cuadro con los valroes que adopta la funcion para valores de m entre
0 y 3 y de n entre 0 y 7"""
def ackermann(m, n):
    if m == 0: 
        return n + 1 
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

for i in range(0, 3):
    for j in range(0, 7):
        print("%4d"%ackermann(i,j), end = " ")
    print()

