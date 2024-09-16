import time
def ajuda():
    sistema = 'Sistema de ajuda PyHELP'
    print('\033[0;34;45m-'* len(sistema))
    print(sistema)
    print('\033[0;34;45m-\033[m'* len(sistema))
    precisoAjuda = str(input('\033[0;34;42m Digite aqui qual função você gostaria de saber mais:\033[m '))
    time.sleep(1.5)
    print('\033[0;34;41m-\033[m' * 35)
    print(f'\033[0;34;41m Acessando as informações de {precisoAjuda}...\033[m')
    print('\033[0;34;41m-\033[m'* 35)
    time.sleep(1.5)
    help(precisoAjuda)
ajuda()