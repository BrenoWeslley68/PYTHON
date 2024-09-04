nome = input('Digite o seu nome aqui: ')
nota1 = int(input('Digite a sua primeira nota aqui: '))
nota2 = int(input('Digite a sua segunda nota aqui: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'{nome}, você foi reprovado, pois a sua media foi {media}')
elif media >= 5 and media < 7:
    print(f'{nome}, você está de recuperação, pois a sua media foi {media}')
else:
    print(f'Parabéns {nome}, você foi aprovado, e a sua media foi {media}')