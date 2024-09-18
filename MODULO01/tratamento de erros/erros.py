try:
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    r = a/b
except(ValueError, TypeError):
    print('Infelizmente tivemos um erro com o valor que você digitou')
except(ZeroDivisionError):
    print('Erro, não é possível dividir um número por 0!')
except(KeyboardInterrupt):
    print('O usuário não diigitou um valor')
else:
    print(f'A divisão entre o numerador {a} e o divisor {b} é {r:.2f}')
finally:
    print('Volte sempre, muito obrigado!')
