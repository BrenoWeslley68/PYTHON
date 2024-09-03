import random
numero = int(input('Digite um número aqui: '))
tenteSorte = int(random.randint(1,5))
if numero == tenteSorte:
    print(f'Parabéns, o número sorteado foi {tenteSorte} e você escolheu {numero}')
else:
    print(f'Infelizmente você perdeu, o número sorteado foi {tenteSorte} e você escolheu {numero}')