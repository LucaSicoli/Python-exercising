"""Desarrollar una funcion eliminarclaves() que reciba como parametros un diccionario y una lista de claves. 
La funcion debe eliminar del diccionario todas las claves contenidas en la lista devolviendo el diccionario modificado y un valor 
de verdad que indique si la operacion fue exitosa. Desarrollar programa"""
def eliminarClaves(dic,claves):
    for clave in claves:
        del dic[clave]
    for clave in dic:
        print(f"{clave}: {dic[clave]}")




dic={"Ornella":"Choclo","Francisco":"Tomate","Serena":"Parrilla","Joaquin":"Paty"}
claves=["Serena","Joaquin"]
eliminarClaves(dic,claves)