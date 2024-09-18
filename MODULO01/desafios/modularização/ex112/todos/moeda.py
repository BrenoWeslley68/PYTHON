import locale

def metade(m, show=True):
    if show:
        return cambio(m / 2)
    else:
        return m / 2
    

def dobro(m, show=True):
    if show:
        return cambio(m * 2)
    else:
        return m * 2

def aumenta(a, b, show=True):
    c = a * b / 100
    c += a
    if show:
        return cambio(c)
    else:
        return c

def diminui(a, b, show=True):
    c = a * b / 100
    a -= c
    if show:
        return cambio(a)
    else:
        return a

def cambio(m):    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = m
    valor_formatado = locale.currency(valor, grouping=True)
    return valor_formatado

def resumo(a, b, c):
    titulo = 'Resumo do valor'
    print('-' * len(titulo))
    print(titulo)
    print('-' * len(titulo))
    print(f'Preço analisado: {cambio(a)}')
    print(f'Dobro do preço: {dobro(a, show=True)}')
    print(f'Metade do preço: {metade(a, show=True)}')
    print(f'{b}% de aumento: {aumenta(a, b, show=True)}')
    print(f'{c}% de redução: {diminui(a, c, show=True)}')

def leiaDinheiro(mensagem):
    while True:
        valor = input(mensagem).replace(',', '.').strip()
        if valor.replace('.', '').isdigit():
            return float(valor)
        else:
            print(f'Erro! "{valor}" não é um valor válido.')