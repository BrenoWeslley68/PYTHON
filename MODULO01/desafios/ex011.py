alturaParede = float(input('Digite a altura da parede aqui: '))
larguraParede = float(input('Digite a largura da parede aqui: '))
tamanhoQuadrado = alturaParede*larguraParede
quantidadeTinta = int(2)
usoTintaNecessario = tamanhoQuadrado/quantidadeTinta
print(f'A altura da parede é {alturaParede} metros, a largura é {larguraParede} metros, o metro quadrado da parede é {tamanhoQuadrado} metros quadrados, para cada {quantidadeTinta} metros é necessário 1 litro de tinta, e o necessário para pintar a parede toda é de {usoTintaNecessario} litros')
