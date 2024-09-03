numero = 1250
def identificarNumero(numero):
    if not isinstance(numero, int) or numero < 0:
        raise ValueError('O número deve ser um inteiro positivo')

    milhar = numero // 1000
    centena = (numero % 1000) //100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    return milhar, centena, dezena, unidade

milhar, centena,dezena,unidade = identificarNumero(numero)
print(f'Numero: {numero}')
print(f'Milhar : {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')


