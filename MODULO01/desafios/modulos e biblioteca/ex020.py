import random
alunos = ['Thiago', 'Eduarda', 'Alexandre', 'Oliveira']
print(f'Os alunos da sala são {alunos} e a ordem de apresentação é:')
random.shuffle(alunos)
for i, aluno in enumerate(alunos, 1):
    print(f'{i}, {aluno}')
