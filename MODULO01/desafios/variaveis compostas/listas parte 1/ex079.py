lista = []
for _ in range(5):
    valores = (int(input('Digite os valores aqui para inseri-los na lista: ')))
    if valores in lista:
        print('Erro, valor já encontrado na lista, não será possível adiciona-lo!')
    else:
        lista.append(valores)
lista.sort()
print(lista)
