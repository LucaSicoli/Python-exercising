tuplavacia=()
tuplaunelemento="hey bro",
tupla="chimichurri", "coronelrojas", "luketin", "luketon",
tupla+=("Mayonesa",)
print(tupla)
binario=(0,1)*3
print(binario)
res=binario[1]+binario[3]
print(res)
estaciones=(21,"septiembre",(21, "junio"))
print(estaciones)
print("La primavera es el", estaciones[0], 'de', estaciones[1])
print('Invierno es el', estaciones[2][0], 'de', estaciones[2][1])
for dato in estaciones:
    print('el datin es: ',dato)
print(estaciones[:2]) 
meses=("setembro", "octubre", "novembro", "decembro")
print("El largo de los meses a partir de septiembre es: ",len(meses))
listita=(12,54,66,88,102)
print(listita)
print("El max es",max(listita))
print("El min es: ", min(listita))
print(sum(listita))
if 12 in listita:
    print("Hey, we found the number 12")
    print("Se encontro en la posicion",listita.index(12))
    print("Se encontro el número 54 ",listita.count(54), "vez")

listaATupla=[2,3,5,9]
print(tuple(listaATupla))
print(list(listaATupla))
a=("Hey", "brother")
b=("Hey", "Sister")
print(a,b)
a,b=b,a
print(a,b)
fecha=(12,"septiembre",2001)
print(fecha)