informacoesPessoas = []
continuar = 'S'
cadastros = 0
maiorPeso = 0
menorPeso = 1000
pessoa = []
while continuar == 'S':
    nome = str(input('Digite o nome da pessoa aqui: '))
    peso = int(input('Digite o peso da pessoa aqui: '))
    continuar = str(input('Deseja continuar? S/N: ')).upper()
    pessoa.append(nome[:])
    pessoa.append(peso)
    informacoesPessoas.append(pessoa[:])
    cadastros += 1
    pessoa = []
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f'A quantidade de pessoas cadastradas foram{cadastros}')
print(f'O maior peso cadastrado foi {maiorPeso} kg')
print(f'O menor peso caastrado foi {menorPeso} kg')
print(informacoesPessoas)

