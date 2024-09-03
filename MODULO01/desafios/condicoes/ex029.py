velocidade = float(input('Digite a sua velocidade'))
velocidadeMaxima = float(80)
valorMulta = (velocidade - velocidadeMaxima) * 7
if velocidade > velocidadeMaxima:
    print(f'MULTADO! Você excedeu o limite de velocidade, o valor da multa a pagar é de R${valorMulta}')
else:
    print(f'Você esta dentro do limite de velocidade, siga em frente!')