valores = 0
continuar = 'S'
media = 0
soma = 0
maior = 0
menor= 999
contador = 0
while continuar == 'S':
    valores = int(input('Digite um valor aqui: '))
    continuar = str(input('Quer continuar? "S" para sim, e "N" para não').upper())
    if valores > maior:
        maior = valores
    if valores < menor:
        menor = valores
    contador += 1
    soma += valores
media = soma / contador
print(f'A média entre todos os valores digitados é igual a: {media}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')

