"""En geometria un vector es un segmento de recta orientado que va desde un punto A hasta un punto B. Los vectores en el plano
se presentan mediante un par ordenado de numero reales (x,y) llamados componentes. Para representarlos basta con unir el origen
de las coordenadas con el punto indicado en sus componentes
Dos vectores son ortogonales cuando son perpendiculares entre si. Paraa determinarlo basta calcular su producto escalar y verificar 
si es == 0. Ej:
A=(2,3) y B=(-3,2) => 2*(-3) + 3*2 = -6 + 6 = 0 => son ortogonales
Escribir una funcion que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o no, tmb un programa"""

def ortogonales(t1,t2):
    a=t1[0]
    b=t1[1]
    c=t2[0]
    d=t2[1]
    op1=a*c
    op2=b*d
    if op1 + op2 == 0:
        print("Son ortogonales")
    else:
        print("No son ortogonales")

t1=int(input("Primer vector; Ingrese un numero: "))
t2=int(input("Primer vector; Ingrese otro numero: "))
t3=int(input("Segunda vector; Ingrese un numero: "))
t4=int(input("Segunda vector; Ingrese otro numero: "))
tupla1=(t1,t2)
tupla2=(t3,t4)
ortogonales(tupla1,tupla2)