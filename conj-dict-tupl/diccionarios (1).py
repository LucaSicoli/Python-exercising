"""Los diccionarios relacionan claves y valores"""
"""AKA arreglos asociativos (PHP), tablas
de hash (Perl) o hashmaps (Java)."""

edades={"Dante":23, "Fran":25, "Orne":20} #los de la derecha son inmutables, o numeros, o cadenas, o tuplas. 
print(edades)
print("la edad de orne es:", edades["Orne"])
print()
colores = {"Rojo":[255,0,0], "Verde":[0,255,0], "Azul":[0,0,255]}
colores = {
"Rojo" : [255,0,0],
"Verde" : [0,255,0],
"Azul" : [0,0,255]
}
dic={x:x**2 for x in range(1,5)}
print("potencia usando diccionario por comprension", dic)

colores["GRIS"]=[128,128,128] #si existia la clave la reemplaza. No puede haber repeticiones, no hay orden interno. 
print(colores)

for color in colores:
    print("Son iterables:"+'\n'+color,"->",colores[color])

if "GRIS" in colores:
    print("Si esta el gris")
if "rojin" not in colores:
    print("El rojin no se encuentra")

a=colores["Rojo"]
b=colores.get("Rojo")
c=colores.get("Rosa")
print("Accedí mediante subindice por nombre", a)
print("Accedí mediante get", b)
print(c)
c=colores.get("Rosa", "not found")
print(c)
print()
print("METODOS")
popmethod=colores.pop("Verde")
print("Metodo POP elimina un elemnto del diccionario y devuelve el valor de la clave, eliminamos verde",popmethod)
claves=list(colores.keys())
print("KEYS devuelve todas las claves", claves)
values=list(colores.values())
print("VALUES devuelve todos los valores, hay que pasar a list", values)
print()
for color, RGBb in colores.items():

    print("ITEMS devuelve una secuencia de tuplas clave:valor",color,"->",RGBb)
print("FROMKEYS convierte cualquier secuencia a diccionario, lista,cadena,tupla,conjunto, cada elemento es una clave, asociado a un none or whatever")
print("No se aplica a variables, se aplica a 'dict', devuelve diccionario")
dias=("lunes","martes")
mes=['enero','febrero']
d1=dict.fromkeys(dias)
print("Esto era una tupla", d1)
d2=dict.fromkeys(mes)
print("Esto era una lista", d2)
vocal="aeiou"
d3=dict.fromkeys(vocal, "mivieja")
print("Esto era un string, dividio letras", d3)

print("DEL elimina un elemento del diccionario o todo el diccionario")
del colores["Rojo"]
print(colores)
try:
    del colores
    print(colores)
except NameError as mensaje:
    print("Se borraron los colores y quedo el diccionario vacio", mensaje)


