frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ', '', )
inverso = junto[::-1]
if junto == inverso:
    print(f'{junto} e {inverso} são PALÍNDROMOS.')
else:
    print(f'{junto} e {inverso} não são PALÍNDROMOS.')
