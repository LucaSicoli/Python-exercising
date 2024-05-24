"""Desarrollar una funcion que devuelva el resto de dos numeros sucesivos
usando restas sucesivas"""
def restaSucesiva(a,b,cociente=0,resto=0):
    if a < b: #porque ya llegamos y el numero quedó mas chico que el divisor
        print(f"El primer numero ingresado dividido {b} da como resultado: {cociente}, el resto es {resto}")
    else: 
        a-=b
        cociente+=1
        resto=a
        restaSucesiva(a,b,cociente,resto)
    
#12 / 2 = 6. 12-2=10. cociente es 1, resto es 10. 10-2=8. cociente
#es 2, resto es 8. 8-2=6. resto es 6 y cociente es 3. 
#6-2=4, resto es 4, cociente es 4. 4-2=2. cociente es 5 y resto es 2
#2-2=0, resto es 0, cociente es 6. 



a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
restaSucesiva(a,b)
