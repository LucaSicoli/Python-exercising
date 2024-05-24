"""Una libreria almacena su lista de precios en un diccionario
Diseñar un programa para crearlo, incrementar los precios de cuadernos en un 15%, 
imprimir un listado con todos los elementos de la lista de precios e indicar cual es
el item mas costoso que venden en el comercio"""
presio={"Calendarios":150, "Lapiceras":1200,"Cuadernos":3400,"Lapiceras Brillito":980,"Pack Microfibras Sharpie":5400}
cuaderno=presio.get("Cuadernos")
porcentaje=(cuaderno/100)*15
cuaderno+=porcentaje
presio["Cuadernos"]=cuaderno
maximo=presio["Cuadernos"]
for producto,precio in presio.items():
    if precio > maximo:
        maximo=precio
        print("El producto con mayor precio es:",producto,"con un valor de",maximo)