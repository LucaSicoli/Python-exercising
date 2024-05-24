"""Desarrollar un programa que use una funcion que reciba como parametro una cadena de caracteres conteniendo una 
direccion de correo electronica y devuelva una tupla con las diferentes partes que componen dicha direccion. Ej:
alguien@uade.edu.ar -> (alguien,uade,edu,ar)"""
def devolverTupla():
    try:
        mail=input("Ingrese un correo electrónico: ")
        assert '@' in mail and '.com' in mail, "Agregue '@', '.' "
        user,dominio=mail.split('@')
        if "ar" in mail:
            dom,com,ar=dominio.split('.')
            tupla=(user,dom,com,ar)
            return tupla
        else:
            dom,com=dominio.split('.')
            tupla=(user,dom,com)
            return tupla
    except AssertionError as mensaje:
        print(mensaje)

tupla=devolverTupla()
print(tupla)


