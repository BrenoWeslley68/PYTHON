nome = input('Digite o seu nome aqui: ')
nomeSemEspacos = nome.replace(' ', '')
nomeCortado = nome.split()
print(f'esse é o seu nome em maiúsculo: {nome.upper()}')
print(f'Esse é o seu nome em minúsculo: {nome.lower()}')
print(f'O seu nome tem um total de letras: {len(nomeSemEspacos)}')
print(f'O seu primeiro nome tem um total de {len(nomeCortado[0])} letras')