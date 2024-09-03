from math import hypot, sqrt
a = 3
b = 4
#hipotenusa = sqrt(a**2 + b**2)
#print(f'O tamanho da hipotenusa é de {hipotenusa}')
hipotenusa = hypot(a,b)
print(f'O valor da hipotenusa é {hipotenusa}')
# Existem essas duas maneiras de se calcular a hipotenusa, é claro que é mais viável utilizar o módulo hypot()
