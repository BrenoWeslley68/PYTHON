import time
def contador(a,b,step):
    if a > b and step > 0:
        step = -step
    if a == 0 and b == 0 and step == 0:
        a = int(input('Digite o valor de A: '))
        b = int(input('Digite o valor de B: '))
        step= int(input('Digite o valor de step: '))
    for c in range(a,b,step):
        print(c)
        time.sleep(0.5)

contador(1,11,1)
contador(10,0,1)
contador(0,0,0)