"""El metodo index permite buscar un elemento dentro de una lista, devlviendo la posicion que este ocupa. 
Sin embargo, si el elemento no pertenece a la lista se produce una excepcion de tipo ValueError.
Desarrollar un programa que cargue una lista con numeros enteros ingresados a traves de teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la posicion que ocupan, usando el metodo index,
Si el numero no pertenece a la lista se imprimira un mensaje de error y se solicitara otro para buscar. 
Abortar el proceso al tercer error detectado. No usar in durante la busqueda"""
while True:
    list=[]
    try:
        num=int(input("Ingrese un número: "))
        while num != -1:
            list.append(num)
            num=int(input("Ingrese un número: "))
        if num == -1:
            break
    except ValueError:
        print("Ingrese numero, no letras.")
print(list)
cont=0
while True: 
    try: 
        buscar=int(input("Ingrese un número de los ingresados a buscar: "))
        encontrado=list.index(buscar)
        if encontrado:
            print(f"{buscar} se encuentra en la posicion {encontrado}")
        else: 
            raise
    except ValueError: 
        print("El numero ingresado no se encuentra dentro de los ingresados.")
        cont+=1
        if cont == 3:
            break
print("Ya has tenido muchos errores, fin del programa.")


        