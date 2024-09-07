import random
contadorVitoria = 0
parOuImpar = 0
while True:
    maquina = random.randint(1,10)
    escollhaOpcao = input('par ou impar? P/I').upper()
    escolha = int(input('Digite um valor de 0 a 10: '))
    parOuImpar = maquina + escolha
    if escollhaOpcao == 'P' and parOuImpar % 2 == 0:
        print('Você venceu!')
        contadorVitoria += 1
    elif escollhaOpcao == 'I' and parOuImpar % 2 == 1:
        contadorVitoria += 1
        print('Você venceu!')
    else:
        print('Você perdeu')
        print(f'A quantidade de vezes que você ganhou foi: {contadorVitoria}')
        break
