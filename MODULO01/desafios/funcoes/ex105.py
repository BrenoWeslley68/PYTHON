def notas(*notas):
    alunos =  {}
    soma = 0
    for valor in notas:
        soma += valor
    media = soma/ len(notas)
    maiorValor = max(notas)
    menorValor = min(notas)
    quantidadeNotas = len(notas)
    alunos['média'] = media
    alunos['Maior valor'] = maiorValor
    alunos['Menor valor'] = menorValor
    alunos['Quantidade de alunos'] = quantidadeNotas
    print(f'A média das notas foram {alunos["média"]}')
    print(f'A quantidade de notas foram {alunos["Quantidade de alunos"]}')
    print(f'A maior nota foi {alunos["Maior valor"]}')
    print(f'A menor nota foi {alunos["Menor valor"]}')
    print(alunos)
notas(5,2,6,5,7,8,9,4,1,2)

