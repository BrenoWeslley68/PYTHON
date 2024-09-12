from random import randint
valorizacao = 5
vezes = int(input('Digite aqui quantos palpites você gostaria que seja gerado: '))
listaAleatoria = []
for c in range(vezes):
    listaNova = [randint(1,100) for c in range(valorizacao)]
    listaAleatoria.append(listaNova)
for i, lista in enumerate(listaAleatoria, 1):
    print(f'A lista {i} tem o valor de {lista}')
    