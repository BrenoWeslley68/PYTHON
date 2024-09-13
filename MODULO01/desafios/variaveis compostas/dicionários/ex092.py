from datetime import datetime
informacoes = {}
precisaContribuir = 35
informacoes['nome'] = str(input('Digite o seu nome aqui: '))
informacoes['ano de nascimento'] = (input('Digite aqui o seu ano de nascimento dd/mm/yyyy'))
informacoes['contratacao'] = input('Digite aqui o ano em que você foi comtratado pela primeira vez: ')
contrata = datetime.strptime(informacoes['contratacao'], '%d/%m/%Y')
nascimento = datetime.strptime(informacoes['ano de nascimento'], '%d/%m/%Y')
dataAtual = datetime.now()
contratacao = dataAtual.year - contrata.year
contribuicao = precisaContribuir - contratacao
idade = dataAtual.year - nascimento.year
aposentadoria = idade + contribuicao
carteiraTrabalho = int(input('Digite o número da sua carteira de trabalho aqui: '))

print(f'O nome é {informacoes['nome']}')
print(f'A idade é {idade}')
if carteiraTrabalho != 0:
    print(f'O numero da sua CTPS é {carteiraTrabalho}')
    print(f'O ano da primeira contratação foi {contrata}')
    print(f'Você vai se aposentar com {aposentadoria} anos')
