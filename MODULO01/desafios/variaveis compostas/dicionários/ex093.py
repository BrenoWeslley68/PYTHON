jogao = {}
jogao['nome'] = str(input('Digite o nome do jogador aqui: '))
partidas = int(input(f'Digite o total de partidas jogadas por {jogao['nome']}: '))
gols = []
contador = 0
total = 0
while contador < partidas:
    gol = int(input('Digite aqui quantos gols foi feito no jogo: '))
    total += gol
    gols.append(gol)
    contador += 1
jogao['gols'] = gols[:]
jogao['total'] = total
print(jogao)
print('______________________________________________________')
print(f'O campo nome teem o valor {jogao["nome"]}')
print(f'O campo gols tem o valor {jogao["gols"]}')
print(f'O campo total tem o valor {total}')
print('________________________________________________')
print(f'O jogador {jogao["nome"]} jogou {partidas} partidas')
for i, gol in enumerate (gols, start= 1):
    print(f'No {i}º jogo {jogao["nome"]} marcou {gol}')     