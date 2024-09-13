'''filme = {
    'Título':'Stars Wars',
    'Ano': '1977',
    'Diretor': 'George Lucas'
}
#print(filme.values()) Mostra os valores Star Wars, 1977 e George Lucas
#print(filme.keys()) Mostra as chaves ou indices titulo, ano, Diretor
#print(filme.items()) Mostra tanto os valores quanto as chaves
pessoas = {
    'nome': 'Breno', 
    'sexo': 'M', 
    'idade': 22
}
pessoas['nome'] = 'Gustavo'
del pessoas['sexo']
pessoas['peso'] = 98.5
print(pessoas['idade'])
for k,v in pessoas.items():
    print(f'{k} = {v}')
    
estado = {
    'uf': 'Rio de Janeiro', 
    'Sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo', 
    'Sigla': 'SP'
}
brasil = []
brasil.append(estado)
brasil.append(estado2)
'''
estado = {}
brasil = []
for c in range(3):
    estado['uf'] = str(input('Digite a uf do estado aqui: '))
    estado['sigla'] = str(input('Digte a sigla do estado aqui: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor de {v}')
        