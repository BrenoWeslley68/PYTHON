def leiaint():
    while True:
        n = input('Digite um número aqui:')
        if n.isdigit():
            n = int(n)
            break
        else:
            print('O valor digitado não é um número!')
    print(f'O número digitado foi {n}')

leiaint()

    