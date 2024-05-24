"""Crear una funcion contarvocales() que reciba una palabra y cuente cuantas letras 
a, e, i, o, u tiene. Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar
a la funcion por cada palabra que contenga la misma. Imprimir cada palabra y cantidad de vocales hallada."""
def contarVocales(palabra):
    vocals=("a","e","i","o","u")
    dic=dict.fromkeys(vocals,0)
    print(dic)
    listaletras=[]
    for letra in palabra:
        if letra in dic:
            dic[letra]+=1
    print(dic)
palabra=input("Ingrese una palabra: ")
contarVocales(palabra)