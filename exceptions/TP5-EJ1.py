"""Desarrollar una funcion para ingresar a traves de teclado un numero natural. La funcion rechazará cualquier 
ingreso invalido de datos usando excepciones y mostrará la razón exacta del error. Controlar que se ingrese un numero,
que ese numero sea entero y que sea mayor que 0.Devolver el valor ingresado cuando este sea correcto.
Escribir tambien un programa que permita probar el correcto funcionamiento."""
while True: 
    try:
        n = int(input("Ingrese un número natural: "))
        assert n >= 0
        break
    except AssertionError:
        print("Debe ingresar un numero positivo")
    except ValueError:
        print("Ingrese un número, no letras por favor")
print(n)
