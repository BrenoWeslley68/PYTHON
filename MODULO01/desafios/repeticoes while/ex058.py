import random
totErrado = 0
digiteNumero = 0
maquinaNumero = 1
while digiteNumero != maquinaNumero:
    digiteNumero = int(input('Digite um número aqui'))
    maquinaNumero = random.randint(1,10)
    print('Errado, tente denovo')
    totErrado += 1
print(f'Certo, você errou {totErrado} vezes até acertar')
