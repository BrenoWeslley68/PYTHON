escolha = 0
maior = 0
novosNumeros = 0

while escolha != 5:
    numero1 = int( input('Digite um valor aqui: '))
    numero2 = int(input('Digite o segundo valor aqui: '))
    escolha = int(input('Digite (1) para somar, digite (2) para multiplicar, digite (3) para saber o maior número, digite (4) para inserir novos números ou digite (5) para sair do programa.'))
    if escolha == 1:
        print(numero1 + numero2)
    elif escolha == 2:
        print(numero1 * numero2)
    elif escolha == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(maior)
    elif  escolha == 4:
        print('Escolha novos números!')
print('Programa finalizado!')
