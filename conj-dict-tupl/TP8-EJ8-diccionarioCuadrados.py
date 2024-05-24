"""Generar e imprimir un diccionario donde las claves sean numeros enteros entre 1 y 20 ambos incluidos
y los valores asociados sean el cuadrado de las claves"""
def generarDiccionario():
    diccionario={x:x**2 for x in range(1,13)}
    print(diccionario)
generarDiccionario()