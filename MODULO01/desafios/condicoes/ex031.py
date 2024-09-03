distancia = float(input('Digite a sua distancia percorrida: '))
distanciaValor50 = distancia *0.5
distanciaValor45 =  distancia * 0.45
print(distanciaValor45)
print(distanciaValor50)
if distancia > 200:
    print(f'A distancia percorrida foi de {distancia} km, e o valor a pagar é de R${distanciaValor45}')
else:
    print(f'A distancia percorrida foi de {distancia} km, e o valor a pagar é de R${distanciaValor50}')
    