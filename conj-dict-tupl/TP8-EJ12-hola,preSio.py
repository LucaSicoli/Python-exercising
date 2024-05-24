"""Una libreria almacena su lista de precios en un diccionario
Diseñar un programa para crearlo, incrementar los precios de cuadernos en un 15%, 
imprimir un listado con todos los elementos de la lista de precios e indicar cual es
el item mas costoso que venden en el comercio"""

precios={"cuadernos":530, "lapiceras":100, "goma":50, "resaltadores color pastel":200, "set microfibras":2530}
print(precios)
cuaderno=precios.get("cuadernos")
porc=(cuaderno/100)*15
cuaderno+=porc
precios["cuadernos"]=cuaderno
max=precios["cuadernos"]
for producto, precio in precios.items():
    if precio > max:
        max=precio
        elem=producto
print("Aumentó el precio de los cuadernos un 15%:", precios)
print(f"El máximo precio lo tiene {elem} con el precio de: {max}")