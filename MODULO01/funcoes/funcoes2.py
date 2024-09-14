'''
Interactive Help
    > help()
        > É o manual de instruções de cada função interna no Python, para acessa-lo basta digitar help() no terminal.

Docstrings
    > É um texo englobado em 3 aspas simples igual a esse aqui, onde você pode documentar o que a sua função faz, caso a pessoa que esteja utilizando ou revisando o seu programa não seja você, a pessoa irá entender.

Argumentos opcionais
    > Se eu declarar uma função com 3 parâmetros, a mesma tem que ter 3 valores, exemplo: a,b,c; a=2, b=3, c=4; caso eu não declare o os 3 parâmetros eu posso fazer o seguinte: def somar(a,b,c=0), isso significa, caso eu passe apenas 2 parâmetros que automaticamente irá para a e b, o parâmetro c valerá 0.

    Eu também posso utilizar essa formatação como padrão sem problema nenhum, se eu não sei quantos parâmetros eu vou receber, eu posso representar todos como 0, exemplo: def somar (a=0, b=0, c=0), nesse caso não ocorrerá erro nenhum, como os parâmetros já foram passados o sistema funcionará corretamente.

Escopo de variáveis
    > O escopo de variável é identico a identação do JS, se uma variável for declarada dentro de uma função e não de forma global, se eu tentar printar a variável na tela fora da função, ela será declarada como indefinida,todavia, se eu declarar de forma global fora da função, a variável funcionará tanto dentro, quanto fora da função.
    Fora de função = Escopo global
    Dentro de função = Escopo local

Retorno de resultados
    >
    '''
def somar(a=0, b=0, c=0):
    s = a +b + c
    return s
r1 = somar(1,2,3)
r2 = somar(4,9)
r3 = somar(8,3)
print(f'A soma dos valores das variáveis s é respectivamente: {r1}, {r2} e {r3}')
