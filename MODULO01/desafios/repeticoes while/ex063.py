primeiroTermo = 0
segundoTermo = 1
termoMaximo = 10
contador = 0
while contador < termoMaximo:
    fibonacci = primeiroTermo + segundoTermo
    contador += 1
    primeiroTermo = segundoTermo
    segundoTermo = fibonacci
    print(fibonacci, end=' ')
