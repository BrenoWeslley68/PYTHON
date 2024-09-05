from datetime import datetime
dataAtual = datetime.now()
maiorIdade = 0
menorIdade = 0
for c in range(7):
    seuNascimento = input('Digite a data de nascimento do aluno aqui: ')
    nascimento = datetime.strptime(seuNascimento, '%d/%m/%Y')
    idade = dataAtual.year - nascimento.year
    if idade < 18:
        menorIdade += 1
    elif idade > 18:
        maiorIdade += 1
print(f'A quantidade de alunos maiores de idade são {maiorIdade}')
print(f'A quantidade de alunos menores de idade são {menorIdade}')
