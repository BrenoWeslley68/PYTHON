matriz = [[],[],[],[],[],[],[],[],[]]
somaPares = 0
somaTerceira = 0
for i in range(9):
    valor = int(input('Digite um valor aqui: '))
    matriz[i].append(valor)
    if valor % 2 == 0:
        somaPares += valor
somaTerceira = sum(matriz[6]) + sum(matriz[7]) + sum(matriz[8])
segundaLinha = max(matriz[3], matriz[4], matriz[5])
print(somaPares)
print(somaTerceira)
print(segundaLinha)
