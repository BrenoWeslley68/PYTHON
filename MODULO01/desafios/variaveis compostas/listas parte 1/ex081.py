lista = []
quantidade = 0
for c in range(10):
    valores = int(input('Digite um valor aqui para adiciona-lo a lista: '))
    quantidade += 1
    lista.append(valores)
    lista.sort(reverse=True)
print(f'A quantidade de valores digitados foram: {quantidade}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista')
else:
    print(f'O valor 5 está na lista!')
print(lista)
