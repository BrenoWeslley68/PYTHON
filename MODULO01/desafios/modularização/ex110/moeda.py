import locale
def metade (m, show=True):
    if show == True:
        return cambio(m / 2)
    else:
        return m/2
    

def dobro (m,show=True):
    if show == True:
        return cambio(m * 2)
    else:
        return m*2

def aumenta(a,b, show=True):
    c = a*b/100
    c += a
    if show==True:
        return cambio(c)
    else:
        return c

def diminui(a,b, show=True):
    c = a * b / 100
    a -= c
    if show==True:
        return cambio(a)
    else:
        return a


def cambio(m):    
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = m
        valorFormatado = locale.currency(valor, grouping=True)
        return valorFormatado

def resumo(a,b,c):
    resumir = 'Resumo do valor'
    print('-'* len(resumir))
    print(resumir)
    print('-'* len(resumir))
    print('-'* len(resumir))
    print(f'Preço analisado: {cambio(a)}')
    print(f'Dobro do preço: {dobro(a,show=True)}')
    print(f'Metade do preço: {metade(a, show=True)}')
    print(f'80% de aumento: {aumenta(a,b, show=True)}')
    print(f'35% de redução: {diminui(a,c, show=True)}')