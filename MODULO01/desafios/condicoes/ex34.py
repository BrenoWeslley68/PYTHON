salario = float(input('Digite o seu salário aqui'))
salárioAcima = salario*10 / 100
salarioAbaixo = salario*15 / 100
if salario < float(1250):
    salarioNovo = salario + salarioAbaixo
    print(f'O seu salario antigo era: R${salario}, o seu aumento foi de R${salarioAbaixo}, e o seu novo salário é de R${salarioNovo}')
else:
    salarioNovo = salario + salárioAcima
    print(f'O seu salário antigo era: R${salario}, o seu aumento foi de R${salárioAcima}, e o seu novo salário é de R${salarioNovo}')
