s = 0
for c in range(6):
    valor = int(input('Digite um valor aqui'))
    s += valor
if s %2 == 0:
    print(f'A soma entre todos os dados fornecidos é de {s}')
else:
    print('')
