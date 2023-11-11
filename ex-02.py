def checkPar(number):
    r = (number%2 == 0)
    return r

def somar_par(lst):
    soma = 0
    for num in lst:
        if checkPar(num):
            if num % 2 == 0:
                soma += num
    return soma

lista = [10,2,4,1,1,1]
soma = somar_par(lista)
print(soma)
