valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor aqui para inserir na lista: ')))
menor = min(valores)
maior = max(valores)
posicaoMaior = valores.index(maior)
posicaoMenor = valores.index(menor)
print(f'O maior valor da lista {valores} foi {maior} e a usa posição foi no indice {posicaoMaior}')
print(f'O menor valor da lista {valores}  foi {menor} e a sua posição no foi no indice {posicaoMenor}')
