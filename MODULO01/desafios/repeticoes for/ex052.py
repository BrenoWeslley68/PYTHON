num = int (input('Digite um número aqui: '))
tot = 0
for c in range(1, num, +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if tot <= 2:
    print(f'O total de vezes que o número {num} foi dividido é {tot}, isso quer dizer que ele é um número primo.')
else:
    print(f'O total de vezes que o número {num} foi dividido é {tot}, isso quer dizer que ele é um número composto.')
