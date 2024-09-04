from datetime import datetime
nome = input('Digite o seu nome aqui: ')
seuNascimento = input('Digite a sua data de nascimento (dd/mm/yyyy) ')
nascimento = datetime.strptime(seuNascimento, "%d/%m/%Y")
dataAtual = datetime.now()
idade = dataAtual.year - nascimento.year
if idade < 10:
    print(f'{nome}, a sua qualificação é Mirim porque você tem {idade} anos')
elif idade >= 10 and idade < 15:
    print(f'{nome}, a sua qualificação é Infantil porque você tem {idade} anos')
elif idade >= 15 and idade <20:
    print(f'{nome}, a sua qualificação é Junior porque você tem {idade} anos')
elif idade == 20:
    print(f'{nome}, a sua qualificação é Sênior porque você tem {idade} anos')
else:
    print(f'{nome}, a sua qualificação é Master porque você tem {idade} anos')