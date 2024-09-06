somaIdade = 0
mediaIdade = 0
MaiorIdade = 0
homemVelho = ''
totMulheres = 0
for p in range(1,5):
    print(f'--{p}º PESSOA--')
    nome = input('Digite o nome da pessoa aqui: ')
    idade = int(input('Digite a idade da pessoa aqui: '))
    sexo = input('Digite o sexo da pessoa aqui [M/F]: ').upper()
    somaIdade += idade
    mediaIdade = somaIdade / 4
    if p == 1 and sexo == 'M':
        MaiorIdade = idade
        homemVelho = nome
    if sexo == 'M' and idade > MaiorIdade:
        MaiorIdade = idade
        homemVelho = nome
    if sexo == 'F' and idade < 20:
        totMulheres += 1
print(f'A média de idade de todas as pessoas é {mediaIdade}')
print(f'O homem mais velho se chama {homemVelho}, porque a sua idade é {MaiorIdade}')
print(f'O total de mulheres mais novas do que 20 anos são {totMulheres}')
