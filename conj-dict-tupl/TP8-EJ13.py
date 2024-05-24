"""Escribir una funcion buscarclave() que reciba como parámetros un diccionario y un valor
y devuelva una lista de claves que apunten("Mapeen") a ese valor en el diccionario, comprobar 
el comportamiento. """
def buscarClave():
        try:
            dic={"frutilla": "roja", "banana":"amarilla", "kiwi":"verde", "uva":"verde"}
            valor=input("Ingrese un valor a buscar: ")
            valores=list(dic.values())
            claves=list(dic.keys())
            lista=[]
            if valor in valores:
                ind=valores.index(valor)
                lista.append(claves[ind])
                print(lista)
        except:
            print("Error")
buscarClave()

