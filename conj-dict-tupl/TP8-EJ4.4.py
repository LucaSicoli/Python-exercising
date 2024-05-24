"""Escribir una funcion que indique si dos fichas de domino encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5, 4)
La funcion devuelve true o false. Escribir programa tb. """
def domino(ficha1,ficha2):
    bandera=False
    fichaUno=set(ficha1)
    fichaDos=set(ficha2)
    """if fichaUno&fichaDos:
        bandera=True
        return bandera
    else:
        return bandera"""
    difSim=fichaUno^fichaDos
    if len(difSim)==2:
        bandera=True
        return bandera
    else:
        return bandera
    
    
    
    
ficha1=int(input("Ingrese un numero para la primer ficha de domino: "))
ficha1bis=int(input("Ingrese otro numero para la primer ficha de domino: "))
ficha2=int(input("Ingrese un numero para la primer ficha de domino: "))
ficha2bis=int(input("Ingrese otro numero para la primer ficha de domino: "))
fichaUno=(ficha1,ficha1bis)
fichaDos=(ficha2,ficha2bis)
bandera=domino(fichaUno,fichaDos)
print(bandera)
