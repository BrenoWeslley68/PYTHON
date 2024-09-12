lista = []
continuar = 'S'
while continuar == 'S':
    nome = str(input('Digite o nome do aluno aqui: '))
    nota1 = float(input(f'Digite a primeira nota de {nome} aqui: '))
    nota2 = float(input(f'Digite a segunda nota de {nome} aqui'))
    aluno = [nome, nota1, nota2]
    lista.append(aluno)
    continuar = str(input('Deseja continuar? S/N: ')).upper()

Aluno = str(input('Digite aqui de qual aluno cadastrado você gostaria de ver a nota: '))
if Aluno == lista[0][0]:
    print(f'A média da nota de {lista[0][0]} foi {(lista[0][1] + lista[0][2]) / 2}')
elif Aluno == lista[1][0]:
    print(f'A média da nota de {lista[1][0]} foi {(lista[1][1] + lista[1][2]) / 2}')
elif Aluno == lista[2][0]:
    print(f'A média da nota de {lista[2][0]} foi {(lista[2][1] + lista[2][2]) / 2}')
elif Aluno == lista[3][0]:
    print(f'A média da nota de {lista[3][0]} foi {(lista[3][1] + lista[3][2]) / 2}')
elif Aluno == lista[4][0]:
    print(f'A média da nota de {lista[4][0]} foi {(lista[4][1] + lista[4][2]) / 2}')
