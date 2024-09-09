'''
lanche.append(''alguma coisa) = insere um novo valor e cria um novo indice no final da lista para esse valor.

lanche.insert(0,'algo') = se ja existir algum item no valor zero e você queira adicionar um novo item no valor zero, sem que precise destruir o seu antecessor, basta adicionar essa função, então será adicionada o novo valor a 0 e o que er zero antes, passará a ser 1.

del lanche[3] remove o valor que está dentro do indice

lanche.remove('algo') remove o valor pelo o seu nome

valores.sort() organiza os valores em ordem crescente

valores.sort(reverse=True) inverte a ordem do sort, o tornando decrescente

'''
num = [1,3,4,6,7,8]
num.append(9)
num.insert(2,2)
num.pop()
print(num)
for c, v in enumerate(num):
    print(f'O indice {c}, armazena o valor {v}')
valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um valor aqui: ')))
print(valores)
b = valores # cria uma ligação com a variável valores, se a variável valores for alterada, o b também será alterada
b = valores[:]# agora sim, cria uma cópia de valores, e se qualquer coisa for alterada em valores, não vai alterar os valores de b
