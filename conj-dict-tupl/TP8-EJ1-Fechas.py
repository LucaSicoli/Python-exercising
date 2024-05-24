"""DesarrolLar las siguientes funciones usando tuplas para representar fechas y horarios y luego escribir un programa
para verificar su comportamiento:
a. ingresar una fecha desde teclado, verificando que corresponda a fecha valida
b.Sumar N dias a una fecha
c.Ingresar un horario desde teclado, verificando que sea correcto
d. calcular la diferencia entre dos horarios. Si el primero fuera mayor al segundo se considerará que
el primero corresponde al dia anterior. En ningun caso la diferencia en horas puede superar las 24 hs."""


def verificarFecha():
    while True:
        try:
            dia=int(input("Ingrese un dia: "))
            assert dia <= 31, "Debe ingresar un mes entre 1 a 31"
            mes=int(input("Ingrese un mes: "))
            assert mes <= 12 and mes >= 1, "Debe ingresar un mes entre 1 a 12"
            año=int(input("Ingrese un año: "))
            assert año >= 2000 and año <= 2100, "Ingrese un año entre el 2000 y 2100"
            tupla=(dia,mes,año)
            return tupla
        except AssertionError as mensaje:
            print(mensaje)

def sumar(tupla):
    while True:
        try:
            dia,mes,año=tupla
            n=int(input("Ingrese un numero para sumar a la fecha: "))
            if dia+n > 31:
                if mes == 12:
                    mes=1
                    restoMes=31-dia
                    restoN=n-restoMes
                    dia=restoN
                    año+=1
                    suma=(dia,mes,año)
                else:
                    mes+=1
                    restoMes=31-dia
                    restoN=n-restoMes
                    dia=restoN
                    suma=(dia,mes,año)
                    tupla=tuple(suma)
            elif dia+n <= 31:
                dia+=n
                suma=(dia,mes,año)
                tupla=tuple(suma)
            return tupla

        except ValueError as mensaje:
            print("Ingrese un numero", mensaje)    

def verificarHorario():
    while True:
        try:
            hora=int(input("Ingrese una hora: "))
            minutos=int(input("Ingrese los minutos: "))
            assert hora < 24, "No hay un dia con mas de 24 hs"
            assert minutos < 59, "No hay una hora con más de 59 minutos"
            horario=(hora,minutos) 
            tupla=tuple(horario)
            return tupla
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError as mensaje:
            print("Ingrese numeros, intente nuevamente", mensaje)

def restarHorarios(horario):
    while True:
        try: 
            hora,minutos=horario
            hora2=int(input("ingrese una hora a restar: "))
            min2=int(input("Ingrese los minutos a restar: "))
            resta=hora-hora2
            resta1=minutos-min2
            restamos=(resta,resta1) #paja calcular lo otro
            print(restamos)
        except ValueError as mensaje:
            print("Ingrese numeros: ", mensaje)


tupla=verificarFecha()
print(tupla)
suma=sumar(tupla)
print(suma)
horario=verificarHorario()
print(horario)
restarHorarios(horario)