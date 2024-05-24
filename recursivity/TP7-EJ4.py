"""Desarrollar una funcion que devuelva el producto de dos numeros
enteros por sumas sucesivas"""
def sumaSucesiva(n1,n2,producto=0):
    if n1==0:
        print(f"La suma de los dos numeros es: {producto}") #se llegó a recorrer todo
    else:
        producto = producto + n2 #0 + 5 (5)-> 5+5=10 (4) -> 10 + 5 (3) -> 15 + 5 (2)-> 20 + 5 (1)-> 25 (0) 
        n1-=1 #4, 3, 2, 1, 0
        sumaSucesiva(n1,n2,producto)


n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro número: "))
sumaSucesiva(n1,n2)