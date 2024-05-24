"""La raiz de un numero puede obtenerse mediante la funcion sqrt() del modulo math. Escribir un programa que utilice 
esta funcion para calcular la raiz cuadrada de un numero cualquiera ingresado a traves del teclado. El programa 
debe usar el manejo de excepcionespara evitar errores si se ingresa un numero negativo."""
import math
from multiprocessing.sharedctypes import Value
while True:
    try:
        n=int(input("Ingrese un numero para obtener su raiz: "))
        assert n > 0
        raiz=math.sqrt(n)
        break
    except AssertionError:
        print("Ingrese un número positivo por favor")
    except ValueError:
        print("No ingrese letras, sólo numeros positivos")
print(raiz)


