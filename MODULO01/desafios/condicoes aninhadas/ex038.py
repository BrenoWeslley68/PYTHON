numero1 = int(input('Digite o primeiro número aqui: '))
numero2 = int(input('Digite o segundo número aqui: '))
if numero1 > numero2:
    print(f'O  primeiro numero {numero1} é maior que o segundo numero {numero2}')
elif numero2 > numero1:
    print(f'O segundo numero {numero2} é maior que o primeiro numero {numero1}')
elif numero1 == numero2:
    print('Ambos os números são iguais')
