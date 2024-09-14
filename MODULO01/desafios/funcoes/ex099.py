def maior(*valores):
    contador = len(valores)
    print(f'Analisando os valores passados...')
    print(f'{valores} Foram informados {contador} valores ao todo')
    print(f'O maior valor informado foi {max(valores)}')

maior(1,2,3,30,5,6,15)