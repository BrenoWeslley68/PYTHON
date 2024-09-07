# as tuplas são imutáveis
lanche = 'hamburguer'
lanche = 'suco' # ao adicionar uma nova atribuição a variável lanche, a anterior será eliminada.
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1])
print(lanche[0:2])
print(lanche[1:])
print(lanche[:2])
print(lanche [-1])# pega o último elemento
print(lanche[-2])# pega o penultimo elemento
print(len(lanche[0]))# mostra qual é o comprimento de letras que o primeiro elemento(hamburguer) tem.
print(len(lanche))# mostra quantos elementos tem a variável lanche
for comida in range(0, len(lanche)):
    print(f'Eu comi {lanche[comida]}')
print(sorted(lanche)) # mostra os elementos da variável em ordem alfabética.
a = (1,2,3,4)
b = (5,6,7,8)
c = a + b # isso apenas somara as variáveis, apenas organizando-as em uma única tupla, seus valores não serão modificados
print(c)
print(c.index(5)) # mostra em qual posição determinado valor da variável se encontra, nesse caso, o valor 5 se encontra no elemento 4

