pessoas = []
pesos = []
idades = []
for c in range(4):
    pessoa = input('Digite o nome da pessoa aqui: ')
    peso = float(input('Digite o peso da pessoa aqui'))
    idade = int(input('Digite a idade da pessoa aqui: '))
    pessoas.append(pessoa)
    pesos.append(peso)
    idades.append(idade)
for i in range(4):
    print(f'O nome da pessoa é {pessoas[i]}, a idade dela é {idades[i]}, e o peso dela é {pesos[i]}')
mediaIdade = (idades[0] + idades[1] + idades[2] + idades[3]) / 4
homemVelho = max(idades)
menosVinte = 0
if idades > 20:
    menosVinte += 1
print(mediaIdade)
print(homemVelho)
print(menosVinte)



