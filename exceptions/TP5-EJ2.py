"""Funcion q reciba como parámetros dos cadenas de caracteres conteniendo numeros reales, sume ambos valores
y devuelva el resultado como un numero real.  Devolver -1 si alguna de las cadenas no contiene un numero valido, 
usando manejo de excepciones para detectar error"""

def sumar(cad1, cad2):
    try:
        cad_a= int(cad1)
        cad_b=int(cad2)
        suma=cad_a+cad_b
        print(suma)
    except ValueError:
        print("-1")



cad1=input("Ingrese numeros reales (del -inf al +inf): ")
cad2=input("Ingrese otro numero reales: ")
sumar(cad1,cad2)

