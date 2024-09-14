from random import randint
numeros = []
def sorteia(*valores):
    contador = 0
    lista = 5
    while contador < lista:
        num = randint(1,100)
        numeros.append(num)
        contador += 1
    print(f'Sorteando {lista} valores da lista: {numeros} PRONTO')
sorteia()
def soma():
    s = 0
    for i in numeros:
        if i % 2 == 0:
            s += i
    print(f'A soma entre todos os números pares da lista teremos: {s}')
soma()
