import moeda
preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10% de {preço} é {moeda.aumenta(preço,10)}')
print(f'Diminuindo 13% de {preço} é {moeda.diminui(preço,13)}')
