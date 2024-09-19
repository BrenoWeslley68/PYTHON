import modulos
import time

modulos.carregarDados()

menu = 'MENU PRINCIPAL'
print('--' * len(menu))
print(menu)
print('--' * len(menu))
while True:
    try:
        print('Escolha uma opção:')
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar uma nova pessoa')
        print('3 - Sair')
        opcao = int(input('Sua opção: '))
        if opcao == 1:
            modulos.verPessoas()
        elif opcao ==2:
            modulos.cadastrar()
        elif opcao == 3:
            time.sleep(1)
            sair = 'SAINDO DO PROGRAMA...'
            print('--' * len(sair))
            print(sair)
            print('--' * len(sair))
            time.sleep(1)
            break
        else:
            print('Opção inválida')
    except:
        print('Erro, Valor não é um número inteiro')

    