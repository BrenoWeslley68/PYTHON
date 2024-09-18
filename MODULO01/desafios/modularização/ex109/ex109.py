from moeda import aumenta, cambio, diminui, dobro, metade
preço = int(input('Digite o preço: R$'))
print(f'A metade de {(preço)} é {(metade(preço, show=True))}')
print(f'O dobro de {(preço)} é {(dobro(preço,show=True))}')
print(f'Aumentando 10% de {(preço)} é {(aumenta(preço,10,show=True))}')
print(f'Diminuindo 13% de {(preço)} é {(diminui(preço,13,show=False))}')
