continuar = 'S'
contador = 0
media = 0
listaPessoas = []
listaMulheres = []
listaMaiores = []

while continuar  == 'S':
    dicionarioPessoas = {}
    nome = str(input('Digite o nome da pessoa aqui: '))
    idade = int(input(f'Digite o a idade de {nome} aqui: '))
    sexo = str(input(f'Digite o sexo de {nome} aqui M/F: ')).upper()

    contador += 1
    media += idade

    dicionarioPessoas['nome'] = nome
    dicionarioPessoas['idade'] = idade
    dicionarioPessoas['sexo'] = sexo

    if sexo == 'F':
        listaMulheres.append(dicionarioPessoas)

    listaPessoas.append(dicionarioPessoas)

    continuar = str(input('Quer continuar? S/N: ')).upper()
media = media/contador
print(f'A quantidade de pessoas cadastradas foram {contador}')
print(f'A média da idade do grupo é {media}')
print(f'A lista com todas as mulheres cadastrada é {listaMulheres}')
for pessoa in listaPessoas:
    if pessoa['idade'] > media:
        listaMaiores.append(pessoa)
print(listaMaiores)
