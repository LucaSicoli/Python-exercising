"""Desarrollar una funcion que reciba un numero binario y lo devuelva convertido a base decimal"""
def convertirBinario(binario, exp):
    if binario == 0:
        return 0 
    else: 
        ultimoDigito=binario%10
        potencia=ultimoDigito*(2**exp)
        return potencia + convertirBinario(binario//10, exp+1)




binario=int(input("Ingrese un numero binario: "))
exp=0
decimal=convertirBinario(binario, exp)
print(decimal)

