"""Escribir una funcion que reciba un numero entero N y devuelva un diccionario con la tabla
de multiplicar de N del 1 al 12. Escribir programa para probar funcion"""
def multiplicar(n):
    diccionario={x:x*n for x in range(1,13)}
    return diccionario

n=int(input("Ingrese un numero para saber su tabla de multiplicar: "))
dic=multiplicar(n)
print(dic)