"""DesarrolLar las siguientes funciones usando tuplas para representar fechas y horarios y luego escribir un programa
para verificar su comportamiento:
a. ingresar una fecha desde teclado, verificando que corresponda a fecha valida
b.Sumar N dias a una fecha
c.Ingresar un horario desde teclado, verificando que sea correcto
d. calcular la diferencia entre dos horarios. Si el primero fuera mayor al segundo se considerará que
el primero corresponde al dia anterior. En ningun caso la diferencia en horas puede superar las 24 hs."""
def validarFecha():
    while True:
        try:
            dia=int(input("Ingrese un día: "))
            assert dia >= 1 and dia <= 31, "Ingrese un día valido"
            mes=int(input("Ingrese un mes: "))
            assert mes >= 1 and mes <= 12, "Ingrese un mes valido"
            año=int(input("Ingrese un año: "))
            assert año >= 2000 and año <= 2999, "Ingrese un año valido"
            break
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Ingrese números")
    tupla=(dia,mes,año)
    print("Fecha válida", tupla)
    return (tupla)

def sumarDias(tupla):
    try:
        sumar=int(input("Ingrese un numero a sumar"))
        dia=tupla[0]
        mes=tupla[1]
        año=tupla[2]
        print(tupla[0]+sumar)
        if tupla[0]+sumar>31:
            if mes < 12:
                restoMes=31-tupla[0]
                dia=sumar-restoMes
                mes+=1
                tupla=(dia,mes,año)
            else:
                restoMes=31-tupla[0]
                print(restoMes)
                dia=sumar-restoMes
                mes=0
                mes+=1
                año+=1
                tupla=(dia,mes,año)
    
        if dia+sumar < 31:
            dia+=sumar
            tupla=(dia,mes,año)
    except AssertionError as mensaje:
            print(mensaje)
    except ValueError:
        print("Ingrese números")
    return tupla

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
            return restamos
        except ValueError as mensaje:
            print("Ingrese numeros: ", mensaje)
tupla=validarFecha()
print(f"Dias sumados: {sumarDias(tupla)}")
horario=verificarHorario()
print(f"Horario válido: {horario}")
resta=restarHorarios(horario)
print(f"El numero ingresados - {horario} : {resta}")