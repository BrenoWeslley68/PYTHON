from random import randint
numero1 = randint(1,10)
numero2 = randint(1,10)
numero3 = randint(1,10)
numero4 = randint(1,10)
lista = [numero1,numero2,numero3,numero4]
maior = max(lista)
menor = min(lista)
print(lista)
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
