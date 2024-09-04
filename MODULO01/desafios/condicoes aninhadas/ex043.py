nome = input('Digite o seu nome aqui: ')
altura = float(input('digite a sua altura aqui (m): '))
peso = float(input('Digite o seu peso aqui (kg): '))
imc = peso / altura**2
if imc <18.5:
    print(f'{nome}, você está abaixo do peso, pois seu IMC é {imc:.2f}')
elif imc >= 18.5 and imc <= 25:
    print(f'{nome}, você está no peso ideal, pois seu IMC é {imc:.2f}')
elif imc > 25 and imc <= 30:
    print(f'{nome}, você está com sobrepeso, pois seu IMC é {imc:.2f}')
elif imc > 30 and imc <= 40:
    print(f'{nome}, você está com obesidade, pois seu IMC é {imc:.2f}')
else:
    print(f'{nome}, você está com obesidade mórbida, pois seu IMC é {imc:.2f}')
