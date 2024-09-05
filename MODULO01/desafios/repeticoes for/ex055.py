pesos = []
for c in range (5):
    peso = float(input('Digite o peso do indivíduo aqui: '))
    pesos.append(peso)

maiorPeso = max(pesos)
menorPeso = min(pesos)
print(maiorPeso)
print(menorPeso)
