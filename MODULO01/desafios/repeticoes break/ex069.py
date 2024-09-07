pessoasMenores = 0
homensCadastro = 0
mulheresMenores = 0
continuar = ''
while True:
    idade = int(input('Digite a idade da pessoa aqui: '))
    sexo = input('M/F: ').upper()
    if sexo == 'M':
        homensCadastro += 1
    if idade < 20:
        pessoasMenores += 1
    if sexo == 'F' and idade < 20:
        mulheresMenores += 1
    continuar = input('Deseja continuar? S/N ').upper()
    if continuar == 'N':
        break
print(f'{pessoasMenores} é o total de pessoas com menos de 20 anos')
print(f'{homensCadastro} é a quantidade de homens cadastrados')
print(f'{mulheresMenores} é a quantidade de mulheres cadastradas com menos de 20 anos')


