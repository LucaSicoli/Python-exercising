"""Ralizar la implementacion recursiva del metodo de seleccion para ordenar una lista de numeros enteros. 
Sugerencia: colocar el elemento mas pequeño en la primera posicion, y luego ordenar la lista con una 
llamada sucesiva. """

#Realizar la implementación recursiva del método de selección para ordenar una
#Iista de números enteros.

#minimo= 2
#lista.remove(minimo) --> [8,5]
#return [minimo]+ ordenarlista(lista) --> [2] + ordenarlista[8,5] = [2,5,8]

#minimo= 5
#lista.remove(minimo) --> [8]
#return [minimo]+ ordenarlista(lista) --> [5] + ordenarlista[8] = [5,8]

#minimo= 8
#lista.remove(minimo) --> []
#return [minimo]+ ordenarlista(lista) --> [8] + ordenarlista[] = [8]
      
      
def recursivo(lista,i,j):
    if i == len(lista):
        return lista
    else:
        if j != len(lista):
            if lista[j]>lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
            j+=1
        else:
            j = 0
            i+=1
        return recursivo(lista,i,j)

# programa principal
    
#lista=[6,3,7,3,675,3,7,8,9,8,0,1,2,3,4,5,5,5,8,3,6]
lista = [8,6,9,2,5,1]
print(recursivo(lista,0,1))  
