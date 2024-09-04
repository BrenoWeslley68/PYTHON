valorEmprestimo = float(input('Digite o valor do empréstimo desejado: '))
informeSalario = float(input('Informe o seu salário aqui: '))
parcelasEmprestimo = int(input('Informe em quantas parcelas você pagará o empréstimo: '))
valorParcela = valorEmprestimo / parcelasEmprestimo
limiteSalario = informeSalario * 30 / 100
if limiteSalario < valorParcela:
    print(f'Empréstimo de R${valorEmprestimo} negado! O valor da parcela excedeu o limite máximo de 30% do seu salário')
    print(f'O valor da parcela ficou em R${valorParcela} e os 30% do seu salário é de R${limiteSalario}')
else:
    print('Parabéns! Empréstimo concedido com sucesso')
    print(f'Valor parcela {valorParcela}, seus 30% de salário cobre R${limiteSalario}')
