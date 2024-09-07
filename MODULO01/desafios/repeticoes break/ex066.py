numero = 0
soma = 0
contador = 0
while True:
    numero = int(input('Digite um número aqui'))
    contador += 1
    soma += numero
    if numero == 999:
        break
print(f'O valor da soma entre todos os números digitados é de {soma - 999}')
print(f'A quantidade de números digitados foi de {contador -1}')
