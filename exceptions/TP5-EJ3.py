"""Desarrollar una funcion que devuelva una cadena de caracteres con el nombre del mes cuyo numero se recibe como 
parámetro los nombres de los meses deberan obtenerse de una lista de cadenas de caracteres inicializada dentro de la funcion. 
Devolver una cadena vacia si el numero de mes es invalido. La deteccion de meses invalidos deberá realizarse a traves de
excepciones"""
def devolverMes():
    try:
        meses=['enero', 'febrero', 'marzo', 'abril','mayo', 'junio','julio', 'agosto','septiembre', 'octubre', 'noviembre', 'diciembre']
        mes = int(input("Ingrese un numero de un mes (1 al 12): "))
        print(meses[mes-1])
    except AssertionError:
        print(' ')
    except ValueError:
        print("Ingrese un numero por favor")
    except IndexError:
        print("Debe escribir un mes hasta el 12")

devolverMes()