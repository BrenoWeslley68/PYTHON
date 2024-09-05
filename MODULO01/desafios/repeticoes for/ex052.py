import math

def valor(numero):
    if numero < 2:
        return False

    for i in range (2, int(math.sqrt(numero)+1)):
        if numero % i == 0:
            return False
    
    return True
numero = 36
if valor(numero):
    print('É um número primo')
else:
    print('É um número composto')

