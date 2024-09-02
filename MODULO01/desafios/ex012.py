valorProduto = float(input('Digite o valor do produto aqui: '))
valorDeconto = int((valorProduto/100)*5)
valorFinal = int(valorProduto - valorDeconto)
print(f'O valor do desconto adquirido foi de R${valorDeconto}, e o valor final do seu produto ficou R${valorFinal}')

