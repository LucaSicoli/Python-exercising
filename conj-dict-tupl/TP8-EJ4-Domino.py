"""Escribir una funcion que indique si dos fichas de domino encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5, 4)
La funcion devuelve true o false. Escribir programa tb. """
def verificarDomino(tupla1,tupla2):
    bandera=False
    conjt1=set(tupla1)
    conjt2=set(tupla2)
    diferenciasim=conjt1^conjt2 
    if len(diferenciasim) == 2:
        bandera=True
        print(bandera, "--> las fichas encajan")
    else:
        print(bandera, "--> las fichas no encajan")
    


t1=int(input("Primer ficha; Ingrese un numero de domino: "))
t2=int(input("Primer ficha; Ingrese otro numero de domino: "))
t3=int(input("Segunda ficha; Ingrese un numero de domino: "))
t4=int(input("Segunda ficha; Ingrese otro numero de domino: "))
tupla1=(t1,t2)
tupla2=(t3,t4)
print(tupla1)
print(tupla2)
verificarDomino(tupla1,tupla2)
