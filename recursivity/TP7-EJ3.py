"""escribir una funcion que devuelva la suma de los primeros N numeros naturales"""
def devolverSuma(num, suma=0): #tiene que estar declarada la suma porque la necesitamos para la recursividad
    if num==0:
        return(suma)
    elif num > 0:
        suma+=num #tenemos que sumar todos los numeros con su anterior, comenzamos con el numero entero
        num-=1 #un numero menos que el ingresado. si 5, 4
        return devolverSuma(num,suma)

try:
    n=int(input("Ingrese un número natural para saber la suma de estos: "))
    if n < 0:
        n=int(input("Ingrese un numero positivo: "))
except ValueError as mensaje:
    print("No ingrese letras", mensaje)
    n=int(input("Ingrese un numero natural: "))

print(devolverSuma(n))
"""si 3 va a ser. 0+1=1.1+2=3+3=6. Si es 6= 0+1,1+2=3+3=6+4=10+5=15+6=21"""


