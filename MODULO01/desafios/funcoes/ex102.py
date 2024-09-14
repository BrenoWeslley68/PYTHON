def fatorial(a,show=True):
    f = 1
    for c in range(a, 0, -1):
        f *= c
        if show == True:
            if c == a:
                print(c, end= ' ')
            else:
                print(f'X {c}', end=' ')
            if c == 1:
                print(f'= {f}')
    if show == False:
        print(f'O valor de fatorial é {f}')
    
fatorial(5, show=True)