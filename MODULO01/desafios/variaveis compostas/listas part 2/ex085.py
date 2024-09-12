listaUnica = []
listaPar = []
listaImpar = []

for p in range(7):
    valores = int(input('Digite um valor desejado aqui: '))
    if valores % 2 == 0:
        listaPar.append(valores)
    else:
        listaImpar.append(valores)

listaPar.sort()
listaImpar.sort()

listaUnica.append(listaPar)
listaUnica.append(listaImpar)

print(listaUnica)
