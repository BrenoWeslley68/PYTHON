decimal = int(input('Digite um número decimal: '))
escolha = str(input(f'Escolha em  qual formatação você quer: hex, oct ou bin '))
hexadecimal = hex(decimal)
octal = oct(decimal)
binario = bin(decimal)
if escolha == 'bin':
    print(f'O valor escolhido em formatação binária é {binario}')
elif escolha == 'hex':
    print(f'O valor escolhido em formatação hexadecimal é {hexadecimal}')
elif escolha == 'oct':
    print(f'O valor escolhido em formatação octal é {octal}')
else:
    print(decimal)
