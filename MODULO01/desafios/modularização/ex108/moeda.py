
import locale
def metade (m):
    return m / 2

def dobro (m):
    return m * 2

def aumenta(a,b):
    c = a*b/100
    c += a
    return c

def diminui(a,b):
    c = a * b / 100
    a -= c
    return a


def cambio(m):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = m
    valorFormatado = locale.currency(valor, grouping=True)
    return valorFormatado


