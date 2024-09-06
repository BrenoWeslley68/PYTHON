'''c =0
while c < 10:
    c += 1
    print(c)
n = 1
while n != 0:
    n = int(input('Digite um número (ou digite 0 para sair): '))
print('Fim')

escolha = 'S'
while escolha == 'S':
    n = int(input('Digite um número: '))
    escolha = input('Quer continuar? S/N ?').upper()
print('fim')'''
par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um número aqui'))
    if n % 2 == 0:
        par += 1
    else:
        impar +=1
print(f'Você digitou {par} numeros pares e {impar} números impares')
