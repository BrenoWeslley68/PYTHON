palavras = ('Aprender', 'explorar', 'ressucitar', 'lavar', 'jantar', 'ousar')
vogais = 'aeiou'
for palavra in palavras:
    vogaisPalavras = [letra for letra in palavra if letra.lower() in vogais]
    print(f'As vogais da palavra {palavra} são: {vogaisPalavras}')
