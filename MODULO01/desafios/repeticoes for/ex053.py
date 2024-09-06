frase = str(input('Digite uma frase aqui: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'{junto} de tras para frente é igual a {inverso}, isso quer dizer que é um palíndromo')
else:
    print(f'{junto} de tras para frente é: {inverso}, isso quer dizer que não é um palíndromo')

