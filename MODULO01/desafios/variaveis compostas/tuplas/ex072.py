numeros = ('um','dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
valor = int(input('Digite um valor entre 1 e 20: '))
if valor >= 1 and valor <=20:
    print(f'O valor do número {valor} em extenso é igual a {numeros[valor - 1]}')
else:
    print('Erro, valor inválido!')
    