from random import randint
jogadores = {'Jogador1': randint(1,6), 'Jogador2': randint(1,6), 'Jogador3': randint(1,6), 'Jogador4': randint(1,6)}
for jogador, valor in jogadores.items():
    print(f'O {jogador} tirou {valor}')
jogadoresOrdenados = [jogadores.items()]
jogadoresOrdenados.sort(key= lambda x: x[1], reverse=True)
print('\n Classificação!')
for i , (jogador,valor) in enumerate (jogadoresOrdenados, start= 1):
    print(f'{i}º lugar: {jogador} com {valor}') 