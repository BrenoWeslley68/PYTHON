def podeFormar(a,b,c):
    return (a + b > c) and (b + c > a) and(a + c > b)

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if podeFormar(reta1,reta2,reta3):
    if reta1 == reta2 == reta3:
        print('Pode se formar um triângulo equilátero')
    else:
        print('Pode formar um triângulo, mas não equilátero')
else:
    print('Não pode formar um triângulo')