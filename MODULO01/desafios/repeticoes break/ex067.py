numero = 0
tabuada = 0
numero = int(input('Digite um valor ou digite um número negativo para sair: '))
while True:
    tabuada += 1
    print(f'{numero} X {tabuada} = {numero*tabuada}')
    if tabuada == 10:
        tabuada = 0
        if tabuada == 0:
            numero = int(input('Digite um valor ou digite um número negativo para sair: '))
    elif numero < 0:
        break
            
    

