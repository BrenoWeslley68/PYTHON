numero = 0
soma = 0
contador = 0
while numero != 999:
    numero = int(input('Digite uym valor aqui'))
    contador += 1
    soma += numero
    
print(f'A soma entre todos os números digitados foi de {soma - 999}')
print(f'A quantidade de números digitados foi de: {contador}')
