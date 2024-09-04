produto = float(input('Insira o valor do produto:'))
parcelas = int(input('Insira a quantidade de parcela'))
forma = (input('Insira sua forma de pagamento: (cartão,dinheiro)'))

aVista = produto * 10 / 100
aVistaCartao = produto * 5 / 100
x3Cartao = produto * 20 / 100

if parcelas > 1 and forma == 'dinheiro' or forma  not in 'dinheiro cartão':
    print('Essa forma de pagamento não existe!')
else:
    if  parcelas == int(1) and forma == 'dinheiro':
        desconto = produto - aVista
        print(f'Você ganhou R${aVista:.2f} de desconto, pois fez um pagamento a vísta, e o valor total da sua compra foi de R$  {desconto:.2f}')
    elif parcelas == int(1) and forma == 'cartão':
        desconto = produto - aVistaCartao
        print(f'Você ganhou R${aVistaCartao:.2f} de desconto, pois fez um pagamento a vísta no cartão, e o valor final da sua compra foi de R${desconto:.2f}')
    elif parcelas == int(2) and forma == 'cartão':
        print(f'A sua compra ficou no valor de R${produto:.2f}, e ganhou 0% de desconto')
    elif parcelas == int(3) and forma == 'cartão':
        juros = produto + x3Cartao
        print(f'Como o seu pagamento foi a prazo em 3 parcelas, você terá que pagar um juros de R${x3Cartao:.2f} a sua compra ficou num valor de R${juros:.2f}')
