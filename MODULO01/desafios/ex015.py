DiasAlugados = int(input('Insira quantos dias você alugou o carro: '))
kmRodado = float(input('insira quantos km você rodou com o veículo: '))
valorAluguelDia = float(150)
valorKM = float(2)
valorDia = DiasAlugados*valorAluguelDia
valorkm = kmRodado * valorKM
valorTotal = valorkm + valorDia
print(f'Você alugou por {DiasAlugados} dias, você rodou {kmRodado} km, o valor total dos dias alug ados é {valorDia}, o valor por ter rodado {kmRodado} km é de {valorkm}, e o valor total a pagar é de {valorTotal}')
