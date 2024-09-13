alunos = {}
alunos['nome'] = str(input('Digite o nome do aluno aqui: '))
alunos['media'] = float(input(f'Digite a media das notas de {alunos['nome']}: '))

print(f'O nome do aluno é {alunos['nome']}')
print(f'A média de {alunos['nome']} foi de {alunos['media']}')
if alunos['media'] < 7:
    print(f'A pessoa cujo o nome é {alunos['nome']} foi reprovado!')
else:
    print(f'A pessoa cujo o nome é {alunos['nome']} foi aprovado!')
