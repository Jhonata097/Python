while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 41)
    print(f'               TABUADA DO {n}')
    print('-' * 41)
    print(f'{n} x  1 = {1 * n:>2}')
    print(f'{n} x  2 = {2 * n:>2}')
    print(f'{n} x  3 = {3 * n:>2}')
    print(f'{n} x  4 = {4 * n:>2}')
    print(f'{n} x  5 = {5 * n:>2}')
    print(f'{n} x  6 = {6 * n:>2}')
    print(f'{n} x  7 = {7 * n:>2}')
    print(f'{n} x  8 = {8 * n:>2}')
    print(f'{n} x  9 = {9 * n:>2}')
    print(f'{n} x 10 = {10 * n:>2}')
    print('-' * 41)
    while True:
        opc = str(input('Quer continuar? [S/N]'
                        '\n>> ')).strip().upper()[0]
        if opc in 'NS':
            break
        else:
            print('Erro! Digite S ou N.')
    if opc == 'N':
        print('TABUADA ENCERRADA...')
        break

