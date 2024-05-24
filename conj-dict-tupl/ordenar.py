"""realizar un programa para ingresar una frase
y mostrar un listado ordenado alfabéticamente
con las palabras que contiene, eliminando las
repetidas y añadiendo junto a cada una
la cantidad de veces que se encontró."""
frase = input("Ingrese una frase:\n")
listadepalabras = frase.split( )
dic = { }
for palabra in listadepalabras:
    if palabra not in dic:
        dic[palabra] = 1
    else:
        dic[palabra] = dic[palabra] + 1
        #PYTHONIZADO dic = { }
        #for palabra in listadepalabras:
        #dic[palabra] = dic.get(palabra, 0) + 1
        listado = [ ]
for p in dic:
    listado.append("> "+p+": "+str(dic[p])+" veces")
    listado.sort( )
for linea in listado:
    print(linea)