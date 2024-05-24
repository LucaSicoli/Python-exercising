"""Escribir una funcion que reciba un numero entero N y devuelva un diccionario con la tabla
de multiplicar de N del 1 al 12. Escribir programa para probar funcion"""
def multiplicar(n):
    multiplica2={x:x*n for x in range(1,12)}
    print(multiplica2)
    
n=int(input("Ingrese un numero: "))
multiplicar(n)