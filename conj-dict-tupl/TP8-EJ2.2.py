"""Escribir una funcion que reciba como parametro una tupla conteniendo una fecha 
(dia,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato 
extendido. Por ejemplo, para 12,10,17 devuelve e"12 de octubre de 2017"
Escribir el programa para el funcionamiento"""
def devolverFecha(tupla):
    meses={1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
    dia=tupla[0]
    mes=tupla[1]
    año=tupla[2]
    if mes in meses:
        m=meses.get(mes)
        print(f"{dia} de {m} de {año}")
    
while True:
    try:
        dia=int(input("Ingrese un dia: "))
        if dia == -1:
            break
        assert dia >= 1 and dia <=31, "ingrese fecha valida"
        mes=int(input("Ingrese un mes: "))
        assert mes >=1 and mes <=12, "ingrese mes valido"
        año=int(input("Ingrese un año: "))
        assert año >=2000 and año <=2999, "inserte un año entre los 2000 y 2999"
        fecha=(dia,mes,año)
        devolverFecha(fecha)
    except AssertionError as mensaje:
        print(mensaje)
    except ValueError:
        print("Ingrese numero: ")
    except IOError:
        print("Error de SO")
print("Fin")