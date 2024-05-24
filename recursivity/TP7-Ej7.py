"""Dados dos numeros enteros no negativos, devolver el resultado de calcular
el Máximo Comun Divisor (tambien llamado DCM) basándose en las siguientes propiedades
MCD(X,X) = X
MCD(X,Y)=MCD(Y,X)
SI X > Y => MCD(X,Y) = MCD(X-Y, Y)
Usando la funcion anterior calcular el MCD de todos los elementos de una lista de numeros enteros, 
sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite usar iteraciones en ninguna etapa del proceso.
"""
