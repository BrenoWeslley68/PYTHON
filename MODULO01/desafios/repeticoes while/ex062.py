numeroValor = int(input('Digite o primeiro termo: '))
termos = 10
razão = 2
contador = 0
total = numeroValor
while contador < termos:
    total += razão
    contador += 1
    print(total)

print(f'A PA de {termos} termos na razão {razão} do valor {numeroValor} é igual {total}')
