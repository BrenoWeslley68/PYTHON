def ficha ():
    nome = str(input('Digite o nome do jogador aqui: '))
    gols = str(input(f'Digite aqui a quantidade de gols que {nome} fez: '))
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols == 0:
        gols = int(0)
    print(f'O jogador {nome} fez {gols} gols')

ficha()