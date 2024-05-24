"""En geometria un vector es un segmento de recta orientado que va desde un punto A hasta un punto B. Los vectores en el plano
se presentan mediante un par ordenado de numero reales (x,y) llamados componentes. Para representarlos basta con unir el origen
de las coordenadas con el punto indicado en sus componentes
Dos vectores son ortogonales cuando son perpendiculares entre si. Paraa determinarlo basta calcular su producto escalar y
verificar si es == 0. Ej:
A=(2,3) y B=(-3,2) => 2*(-3) + 3*2 = -6 + 6 = 0 => son ortogonales
Escribir una funcion que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o no, tmb un programa"""
def ortogonales(vec1,vec2):
    a=vec1[0]
    b=vec1[1]
    c=vec2[0]
    d=vec2[1]
    mult=a*c
    mult2=b*d
    if mult+mult2 == 0:
        print("son ortogonales")
    else:
        print("no son ortogonales")

a=int(input("Ingrese un numero de la recta x: "))
b=int(input("Ingrese un numero de la recta y: "))
c=int(input("Ingrese otro numero de la recta x: "))
d=int(input("Ingrese otro numero de la recta y: "))
vec1=(a,b)
vec2=(c,d)
ortogonales(vec1,vec2)
