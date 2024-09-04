for c in range(1,100):# Conta de 1 até 99, pois a ultima unidade em python nunca é englobada
    print(c)
print('fim')

for c in range(100, 0 , -1): # conta de 100 até 1, tirando -1 em cada operação
    print(c)

for c in range(0 , 100 , 2): # conta de 0 até 99 pulando de 2 em dois
    print(c)

n = int(input("Digite um número aqui: "))
for c in range(0, n):
    print(c)

i = int(input('Digite um número aqui: ')) # define o valor inicial da repetição
f = int(input('Digite outro número aqui: ')) # define o valor final da repetição
p = int(input('Digite um outro número aqui: '))# define o valor de quantas casas ele vai pular em cada repetição
for c in range(i, f, p):  # a primeira casa sempre será o início, a segunda o fim, e a terceira a iteração, ou seja, o que vai fazer, se vai diminuir (-1), se vai pular de dois em dois (2) etc...
    print(c)

s = 0 # define o valor da variável s como 0
for c in range(0,3): #cria um laço de repetição de 3 vezes
    n = int(input('Digite um número aqui: '))# cria um input em números inteiros para o usuário interegir
    s += n # essa equação faz com que em cada repetição s receba ele mesmo, mais n
print(s) # aparece o resultado da soma de n recebido em s
print('Fim')

