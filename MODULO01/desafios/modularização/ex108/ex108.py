from moeda import aumenta, cambio, diminui, dobro, metade
preço = int(input('Digite o preço: R$'))
print(f'A metade de {cambio(preço)} é {cambio(metade(preço))}')
print(f'O dobro de {cambio(preço)} é {cambio(dobro(preço))}')
print(f'Aumentando 10% de {cambio(preço)} é {cambio(aumenta(preço,10))}')
print(f'Diminuindo 13% de {cambio(preço)} é {cambio(diminui(preço,13))}')
