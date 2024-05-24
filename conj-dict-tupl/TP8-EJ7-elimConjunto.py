"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos 
del conjunto mediante el metodo remove, mostrando el contenido del conjunto luego de cada eliminación. 
Finalizar el proceso al ingresar -1. Usar el manejo de excepciones para evitar quitar elementos inexistentes"""
def eliminarElemento(conjunto):
    while True:
        try:
            for elemento in conjunto:
                print(elemento,end="-> ")
            dele=int(input("\nIngrese un número del conjunto para eliminar: "))
            if dele != -1:
                conjunto.remove(dele)
                print(f"Número eliminado, conjunto: {conjunto}")
            else:
                break
            if len(conjunto)==0:
                print("No quedaron mas elementos en el conjunto")
                break
        except KeyError:
            print("El elemento ingresado no existe en el conjunto, intente nuevamente: ")
    print("Finished")


conjunto=set(range(10))
eliminarElemento(conjunto)