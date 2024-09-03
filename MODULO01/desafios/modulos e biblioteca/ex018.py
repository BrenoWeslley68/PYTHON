import math;
angulo = float(input('Digite o angulo desejado: '))
anguloRadianos = math.radians(angulo)

seno = math.sin(anguloRadianos);
cosseno = math.cos(anguloRadianos);
try:
    tangente = math.tan(anguloRadianos)
except ValueError:
    tangente = 'indefinido'

print(f'O valor de seno é {seno}')
print(f'O valor de cosseno é {cosseno}')
print(f'O valor de tangente é: {tangente}')
