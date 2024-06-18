def voto():
    ano = int(input('Ano de nascimento: '))
    idade = 2024 - ano
    if idade < 18:
        print(f'Com {idade} anos: AINDA NÃO VOTA!')
    if 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    if idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')


voto()