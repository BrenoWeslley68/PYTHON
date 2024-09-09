lista = []
listaPar = []
listaImpar = []
for c in range (15):
    valores = int(input('Digite um valor aqui para adiciona-lo na lista'))
    lista.append(valores)
    if valores % 2 == 0:
        listaPar.append(valores)
    else:
        listaImpar.append(valores)
print(f'A lista completa com todos os valores digitados é {lista}')
print(f'A lista contendo todos os valores pares é {listaPar}')
print(f'A lista contendo todos os valores impares é {listaImpar}')