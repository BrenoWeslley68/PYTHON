nome = input('Digite o seu nome aqui: ')
n1 = float(input('Digite aqui a primeira nota: '))
n2 = float(input('Digite aqui a segunda nota: '))
n3 = float(input('Digite aqui a terceira nota: '))
n4 = float(input('Digite aqui a quarta nota: '))
n5 = float(input('Digite aqui a quinta nota: '))
media = (n1 + n2 + n3 + n4 + n5) / 5
if media <= 6:
    print(f'A media das suas notas foi {media}, e você foi reprovado {nome}!')
else:
    print(f'Parabéns, a média das suas notas foi {media}, e  você foi aprovado {nome}!')