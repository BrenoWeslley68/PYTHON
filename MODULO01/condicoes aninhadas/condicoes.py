nome = str(input('Digite o seu nome aqui: '))
if nome == 'Breno':
    print('Que nome bonito você tem')
elif nome == 'Pedro' or nome == 'João' or nome == 'Gustavo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Jessica Eliane Joice':
    print('Belo nome feminino')
else:
    print('Seu nome é bem comum')
print(f'Bom dia, {nome}')