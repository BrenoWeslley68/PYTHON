import lista

def carregarDados():
    try:
        with open('dados.txt', 'r') as arquivo:
            for linha in arquivo:
                if linha.strip():
                    dados = linha.strip().split(',')
                    if len(dados) == 2:
                        nome, idade = dados
                        lista.listaCadastro.append(nome)
                        lista.listaCadastro.append(int(idade))
        print('Dados carregados com sucesso!')
    except FileNotFoundError:
        print('Nenhum arquivo encontrado, o arquivo será criado ao adicionar novos dados.')

def verPessoas():
    if not lista.listaCadastro:
        print('Nenhuma pessoa cadastrada')
        return
    titulo = 'PESSOAS CADASTRADAS'
    print('-' * len(titulo))
    print(titulo)
    print('-' * len(titulo))
    print(lista.listaCadastro)

def cadastrar():
    nome = str(input('Digite o nome da pessoa aqui: '))
    print(f'O nome {nome} foi adicionado!')
    idade = int(input('Digite a idade da pessoa aqui: '))
    print(f'A idade {idade} foi adicionado!')
    lista.listaCadastro.append(nome)
    lista.listaCadastro.append(idade)
    with open ('dados.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {idade}\n')


def listagem():
    print(lista.listaCadastro)


