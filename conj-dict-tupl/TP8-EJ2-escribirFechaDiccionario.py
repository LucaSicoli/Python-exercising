"""Escribir una funcion que reciba como parametro una tobla conteniendo una fecha 
(dia,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato 
extendido. Por ejemplo, para 12,10,17 devuelve e"12 de octubre de 2017"
Escribir el programa para el funcionamiento"""
def escribirFecha():
    try: 
        meses={1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 9:"septiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}
        dia=int(input("Ingrese un dia: "))
        mes=int(input("Ingrese un mes: "))
        año=int(input("Ingrese un año: "))
        assert dia <= 31, "ingrese un dia del 1 al 31"
        assert mes <= 12, "ingrese un mes del 1 al 12"
        assert año >=10 and año<=99, "ingrese un año mayor a '09 y menor a '99"
        if mes in meses:
            m=meses.get(mes)
            veinte='20'
            suma=veinte+str(año)
            print(f"{dia} de {m} de {suma}")
    except ValueError as mensaje:
        print("Ingrese numeros", mensaje)
    except AssertionError as mensaje:
        print(mensaje)

escribirFecha()