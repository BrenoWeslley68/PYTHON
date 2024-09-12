pessoas = []
pessoa1 = ['João', 25]
pessoa2 = ['Maria', 32]
pessoa3 = ['Eduarda', 18]
pessoas.append(pessoa1[:])
pessoas.append(pessoa2[:])
pessoas.append(pessoa3[:])
print(pessoas[0][0])
for pessoa in pessoas:
    print(pessoas)