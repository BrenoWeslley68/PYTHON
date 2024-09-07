saque = int(input('Digite o valor do saque desejado: '))
nota50 = 50
vezes50 = 0
nota20 = 20
vezes20 = 0
nota10 = 10
vezes10 = 0
nota1 = 1
vezes1 = 0
while True:
    if saque >= nota50:
        saque -= nota50
        vezes50 += 1
    elif saque < nota50 and saque >= nota20:
        saque -= nota20
        vezes20 += 1
    elif saque < nota20 and saque >= nota10:
        saque -= nota10
        vezes10 += 1
    elif saque < nota10 and saque >= nota1:
        saque -= nota1
        vezes1 += 1
    elif saque < nota1 or saque == 0:
        break
print(f'Foram {vezes50} notas de 50 reais')
print(f'Foram {vezes20} notas de 20 reais')
print(f'Foram {vezes10} notas de 10 reais')
print(f'Foram {vezes1} notas de 1 real')

