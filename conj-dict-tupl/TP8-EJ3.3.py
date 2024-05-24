"""Desarrollar un programa que use una funcion que reciba como parametro una cadena de caracteres conteniendo una 
direccion de correo electronica y devuelva una tupla con las diferentes partes que componen dicha direccion. Ej:
alguien@uade.edu.ar -> (alguien,uade,edu,ar)"""
def devolverMail(mail):
    usuario,dominio=mail.split("@")
    if "ar" in mail:
        dom,com,ar=dominio.split('.')
        tupla=(usuario,dom,com,ar)
        return tupla
    else:
        dom,com=mail.split('.')
        tupla=(usuario,dom,com)


mail=input("Ingrese su mail: ")
tupla=devolverMail(mail)
print(tupla)
