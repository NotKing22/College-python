def calcFatorial(n):
    resultado = 0
    for numero in range(n):
        numero = numero*(numero-1)
        resultado = numero
        if (numero == 0):
            print("fatorial feito")
    return resultado

x = 3;
calcFatorial(x)