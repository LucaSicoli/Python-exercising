"""Escribir una funcion buscarclave() que reciba como parámetros un diccionario y un valor
y devuelva una lista de claves que apunten("Mapeen") a ese valor en el diccionario, comprobar 
el comportamiento. """
def buscarClave(diccionario,buscar,lista=[]):
    for ingrediente,comida in diccionario.items():
        if buscar in comida:
            lista.append(ingrediente)
    print(lista)
    
dic={"Choclo":"Tarta","Champignon":"Salsa","Mostaza":"Pollo","Barbacoa":"Mascarpone","Papas":"Mascarpone",}
valor=input("Ingrese un valor a buscar")
buscarClave(dic,valor)