"""escribir un programa que juegue con el usuario a adivinar un numero, debe generar un numero 
al azar entre 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se ingrese un valor se muestra
un mensaje indicando si el numero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, se debe
imprimir en pantalla la cantidad de intentos que le tomo hallar el numero. Si el usuario introduce algo que no sea
un numero, se mostrara un mensaje en pantalla y se lo contará como un intento mas."""
import random
def adivinarNum(aleatorio):
    cant=1
    try:
        num=int(input("Adivine el número: "))
        while num != aleatorio:
            cant+=1   
            if num>aleatorio:
                print("El número que debes adivinar es menor a ", num)
            elif num<aleatorio:
                print("El número que debes adivinar es mayor a ", num)
            num=int(input("Adivine el número: "))
    except ValueError:
        print("¡ERROR! No se ha ingresado un número o ingresó uno con decimales. Por favor, intente nuevamente.")
    print("¡ADIVINÓ EL NÚMERO! la cantidad de intentos fueron:",cant)     
aleatorio= random.randint(1,500) 
print(aleatorio)
adivinarNum(aleatorio)
