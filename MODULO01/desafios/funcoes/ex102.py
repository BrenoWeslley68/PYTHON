def fatorial(a, show=True):
    f = 1
    for c in range(a, 0, -1):
        f *= c 
    if show == True:
        print(f'O processo de resolução do fatorial é: ')
        for i in range(1,a +1):
            if i < a:
                print(f'{i} X', end=' ')
            else:
                print(i, end=' ')
        print(f' = {f}')
    else:
        print(f'O resultado o fatorial de 5 é {f}')

fatorial(5, show=False)