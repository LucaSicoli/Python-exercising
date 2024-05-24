"""Ingresar desde teclado una frase y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una
Finalmente mostrar las palabras ordenads segun su longitud."""
def ordenarFrase(frase):
    splitted=frase.split(" ")
    conjunto=set(splitted)
    print(conjunto)
    tupla=tuple(conjunto)
    palabras=[]
    for palabra in tupla:
        palabras.append(palabra)
    palabras.sort(key=len)
    return palabras


frase=input("Ingrese una frase: ")
ordenada=ordenarFrase(frase)
print(ordenada)
