'''def lin():
    print('-'*30)

lin()
print('    BRENO WESLLEY    ')
lin()
lin()
print('    IRINEU ALVES     ')
lin()
lin()
print('    JUBELEU ALMEIDA     ')
lin()
'''
def mensagem(txt):
    print('-' *30)
    print(txt)
    print('-'*30)


mensagem('Olha esse texto aqui')
mensagem('Python é muito legal')

def soma(a,b):
    print(f'O valor de A é {a} e o valor de B é {b}')
    s = a+b
    print(f'O valor da soma entre A + B é {s}')
    print(' ')


soma(4,5)
soma(9,3)
soma(5,6)

def contador (*núm):
    tam = len(núm)
    print(f'Os valores apresentados são {núm} e ao todo são {tam} valores')

contador(1, 5, 4, 8)
contador(1,5,6,4)
contador(5,4,9,8,7)

valores = [2,4,5,8,6,3,8,7]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1
    print(valores)
dobra(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'A soma entre os valores{valores} é {s}')
soma(2,4,5,6)
soma(9,8,7,6)