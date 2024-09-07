nome = ''
preco = 0
continuar = 'S'
valorTotal = 0
maisMil = 0
maisBarato = 999
nomeMaisBarato = ''
while True:
    nome = input('Digite o nome do produto aqui: ')
    preco = float(input('Digite o preço do produto aqui em formato 0.00: '))
    continuar = input('Deseja continuar? S para sim, N para não: ').upper()
    valorTotal += preco
    if preco > 1000:
        maisMil += 1
    if preco < maisBarato:
        nomeMaisBarato = nome
    if continuar != 'S':
        break
print(f'O valor total gasto na compra foi de R${valorTotal}')
print(f'a quantidade de produtos que custam mais de R$1000.00 são: {maisMil}')
print(f'O nome do produto mais barato é: {nomeMaisBarato}')
