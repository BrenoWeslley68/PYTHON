'''
Modularização:
    > Surgiu no início da década de 60
    > Sistemas ficando cada vez maiores
    > Foco: dividir um programa grande
    > Foco: aumentar a legibilidade
    > Foco: facilitar a manutenção
     
def fatorial (n):
    f = 1
    for c in range(n, 1, -1):
        f *= c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

vantagens:
    > Organização do código
    > Facilita a manutenção
    > Ocultação do cód detalhado
    > Reutilização do cód para outro projeto
    
'''
from uteis import numeros
num = int(input('Digite um valor: '))
dobro = numeros.dobro(num)
triplo = numeros.triplo(num)
fat = numeros.fatorial(num)
print(f'O valor que você escoleu foi {num} e o seu fatorial é {fat}, o seu dobro é {dobro} e o seu triplo é {triplo}')
