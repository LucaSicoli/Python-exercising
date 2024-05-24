"""Ingresar desde teclado una frase y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una
Finalmente mostrar las palabras ordenads segun su longitud."""
frase=input("Ingrese una frase: ")
separada=frase.split()
conj=set(separada)
tupla=tuple(conj)
palabrasLargo=[]
for palabra in tupla:
    palabrasLargo.append(palabra)
palabrasLargo.sort(key=len)
print(palabrasLargo)

