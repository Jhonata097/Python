palavras = ('Olá', 'Mundo', 'Droga', 'Inútil', 'Desânimo', 'Depressão', 'Aralho')
for p in palavras:
    print(f'\nNa palavra {p} as vogais são:', end=' ')
    for letra in p:
        if letra.lower() in 'aáâãeéêiíoóôuú':
            print(f'{letra.lower()}', end=' ')
