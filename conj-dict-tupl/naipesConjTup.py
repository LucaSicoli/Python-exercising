"""Desarrollar un programa para simular
la entrega de naipes a un jugador de
póker, evitando la generación de
naipes repetidos."""
import random
simbolo= ("Trebol", "Pica", "Corazon", "Diamante") #Tupla porque está entre parentesis, permite que se repitan y tiene un orden
mano=set() #como no se pueden repetir hacemos un conjunto vacio.
intentos=0 #cant de veces que conseguimos cartas unicas (5)
while len(mano)<5:
    numero=random.randint(1,13) #1 a 10 + j q k 
    palo=random.randint(0,3) #4 simbolos o palos, subindice. 
    carta=(numero,simbolo[palo]) #elige un numero de carta, un simbolo indicado por su subindice palo
    mano.add(carta) #vamos a agregar la carta en el conjunto, como van a estar mezcladas las 5, ademas no permite repetidos
    intentos+=1
print(mano)
print("Intentos realizados, asi sabemos cuantas veces se intentó y se repitió: ", intentos)
