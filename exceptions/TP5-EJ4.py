"""todo programa python es suceptible de ser interrumpido mediante la pulsacion de las teclas Ctrl-C,
lo que genera una excepcion de tipo keyboardinterrupt. Realizar un programa para imprimir los numeros entre 1 y 100000,
y que solicite información al usuario antes de detenerse cuando se presione Ctrl-C"""
for i in range(1,100000):
    try:
        print(i)
    except KeyboardInterrupt:
        print("Desea interrumpir el programa?")
        interrupt = int(input("Sí(1)/No(0)"))
        if interrupt == 1:
            raise
        else:
            pass