import random
minhaEscolha = input('Escolha entre: pedra, papel ou tesoura').lower()
escolhaMaquina = ['pedra', 'papel', 'tesoura']
maquina = random.choice(escolhaMaquina)
print(maquina)
if minhaEscolha not in escolhaMaquina:
    print('Erro, não existe essa alternativa!')
else:
    if (minhaEscolha == 'pedra' and maquina == 'papel') or (minhaEscolha == 'papel' and maquina == 'tesoura') or (minhaEscolha == 'tesoura' and maquina == 'pedra'):
        print(f'Eu perdi, porque a minha escolha foi {minhaEscolha} e a maquina escolheu {maquina}')

    elif (minhaEscolha == 'pedra' and maquina == 'tesoura') or (minhaEscolha == 'papel' and maquina == 'pedra') or (minhaEscolha == 'tesoura' and maquina == 'papel'):
        print(f'Eu venci, porque minha escolha foi {minhaEscolha} e a escolha da maquina foi {maquina}')
    else:
        print(f'foi empate, porque eu escolhi {minhaEscolha}, e a máquina escolheu {maquina}')

