jogao = []
continuar = 'S'
partidas = 10
totGols = 0
listaGol = []

while continuar == 'S':
    jogadores = {}
    contador = 0
    listaGol = []
    totGols = 0
    nome = str(input('Digite aqui o nome do jogador: '))
    partidas = int(input(f'Digite aqui quantas partidas {nome} jogou: '))
    jogadores['nome'] = nome

    while contador < partidas:
        gols = int(input(f'Digite aqui quantos gols {nome} fez na partida: '))
        totGols += gols
        contador += 1
        listaGol.append(gols)
    jogadores['gols'] = listaGol
    jogadores['total'] = totGols
    jogao.append(jogadores)
    continuar = str(input('Quer continuar? S/N: ')).upper()
for jogador in jogao:
    print(f'Nome jogador {jogador['nome']}')
    print(f'O numero de gols por partida do jogador foi {jogador['gols']}')
    print(f'O total de gols desse jogador foi {jogador['total']}')
    print('_________________________________________________')



