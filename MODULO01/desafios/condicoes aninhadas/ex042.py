def formas(a,b,c):
    return (a + b > c), (b + c > a), (c + a > b)
reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))

if formas(reta1, reta2, reta3):
    if reta1 == reta2 == reta3:
        print('De acordo com o valor digitado, você formou um triângulo Equilátero')
    elif reta1 != reta3 == reta2 or reta1 != reta2 == reta3 or reta2 != reta1 == reta3 or reta2 != reta3 == reta1 or reta3 != reta1 == reta2 or reta3 != reta2 == reta1:
        print('De acordo com o valor digitado, você formou um triângulo Isóceles')
    else:
        print('De acordo com o valor digitado, você formou um triângulo Escaleno')