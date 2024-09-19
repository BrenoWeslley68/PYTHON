def leiaInt():
    while True:
        try:
            n = int(input('Digite um valor inteiro válido aqui: '))
            print(f'O valor de n é {n}')
            break
        except:
            print('O valor digitado é inválido')

leiaInt()

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um valor real aqui: '))
            print(f'O valor de n é {n}')
            break
        except:
            print('O valor digitado é inválido!')
leiaFloat()