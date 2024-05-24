#no permiten elementos repetidos
frutti={"mela","banana","l'uva","arancio","arancio"} 
print(frutti) #sin orden 
conjunto=set() #conjunto vacio
#No se puede introducir listas, tuplas, strings dentro de los conjuntos. 
#son mutables, pueden ser modificados.
#los elementos dentro son inmutables, como los numeros, strings o tuplas
if "mela" in frutti:
    print("La mela é una frutta")
if "corazon" not in frutti:
    print("El corazon no está aquí")

comida={"sorrentino", "choclo"}
bebida={"coca","agua"}
print(comida,bebida)
animali={'gatti','canni'}
favoritos={'gatti','loro'}
print(animali, favoritos)
print()
print()


print("OPERACIONES CON CONJUNTOS")
suma=comida|bebida #UNION
print("la suma de los dos conjuntos |",suma)
interseccion=animali&favoritos #LOS ELEMENTOS QUE COMPARTEN
print("los que tienen en comun &",interseccion)
diferencia=animali-favoritos
print("Eliminamos del primer conjunto los que se repiten -",diferencia)
diferenciasim=animali^favoritos 
print("Agarra de ambos los que no comparten y los une ^ ", diferenciasim)
print()
print()

print("FUNCIONES CON CONJUNTOS:")
a={1,5,6,3,9}
print(a)
print("El largo del conjunto es: ", len(a))
print("El elemento mas pequeño es", min(a))
print("El elemento mas grande es", max(a))
print("La suma es: ", sum(a))

print()
print("SE PUEDEN RECORRER CON UN FOR")
conj=set(range(10)) #creamos un conjunto y le mandamos 10 numeros
for elem in conj:
    print(elem,end="--")

print("ADD AGREGA ELEMENTO AL CONJUNTO")
conj.add(12)
print("agregamos el 12",conj)
print("REMOVE elimina elemento identificado por valor, con error")
conj.remove(12)
print("Eliminamos el 12: ",conj)
print("DISCARD elimina elemento identificado por valor, sin error")
conj.discard(9)
print("Eliminamos el 9: ",conj)
print("POP elimina elemento, CON error, elimina al azar")
conj.pop()
print("Eliminamos al azar: ",conj)
print("CLEAR elimina todo el conjunto, lo deja en set. Vacio")
conj.clear()
print(conj)

