lista = []

for c in range(10):
    valores = int(input('Digite um valor aqui para adiciona-lo a lista: '))
    posicao = 0
    while posicao < len(lista) and valores > lista[posicao]:
        posicao +=1
    lista.insert(posicao, valores)
print(lista)