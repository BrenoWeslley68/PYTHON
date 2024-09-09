
valor1 = int(input('Digite o primeiro valor aqui: '))
valor2 = int(input('Digite o segundo valor aqui: '))
valor3 = int(input('Digite o terceiro valor aqui: '))
valor4 = int(input('Digite o quarto valor aqui: '))
valores = (valor1,valor2, valor3, valor4)
nove = valores.count(9)
tres = valores.index(3)
if valor1 % 2 == 0:
    print(valor1)
if valor2 % 2 == 0:
    print(valor2)
if valor3 % 2 == 0:
    print(valor3)
if valor4 % 2 == 0:
    print(valor4)
print(f'O valor 9 apareceu {nove} vezes')
print(f'O valor 3 foi avistado a primeira vez no índice {tres}')
