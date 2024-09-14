from datetime import datetime
def voto(votacao):
    dataAtual = datetime.now().year
    idade = dataAtual - anoNascimento
    print(idade)
    if idade <= 17:
        print(f'Você tem {idade} anos por isso você não pode votar')
    elif idade >= 18 and idade < 60:
        print(f'O seu voto é obrigatório porque você tem {idade} anos')
    else:
        print(f'O seu voto é opcional, porque você tem {idade} anos')
anoNascimento = int(input('Digite o seu ano de nascimento: '))
voto(anoNascimento)
