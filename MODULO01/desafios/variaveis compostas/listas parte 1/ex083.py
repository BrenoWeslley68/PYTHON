expressao = input('Digite uma expressão aqui: ')
parentesesDireita = expressao.count(')')
parentesesEsquerda = expressao.count('(')
if parentesesEsquerda != parentesesDireita:
    print('Expressão inválida!')
else:
    print(expressao)

