n = int(input('Digite um valor aqui para saber o seu fatorial: '))
fatorial = 1
if n < 0:
    print('Não é possível realizar o fatorial de um número negativo')
elif n == 0 or n == 1:
    print(f'O valor do fatorial de {fatorial} é 1')
else:
    while n != 0:
        fatorial *= n
        n += -1
print(fatorial)
