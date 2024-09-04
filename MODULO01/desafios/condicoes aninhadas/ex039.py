from datetime import datetime
nome = input('Digite o seu nome aqui: ')
nascimentoInput = input('Digite a sua data de nascimento aqui (dd/mm/yyyy)')
nascimento = datetime.strptime(nascimentoInput, "%d/%m/%Y")
dataAtual = datetime.now()
idade = dataAtual.year - nascimento.year
if idade < 18:
    prazo = 18 - idade
    print(f'{nome}, ainda não é hora para se alistar, faltam {prazo} anos ')
elif idade == 18:
    print(f'{nome}, está na hora de você se alistar')
else:
    prazo = idade - 18
    print(f'{nome}, você está atrasado para o alistamento militar há {prazo} anos')