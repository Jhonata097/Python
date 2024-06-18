n = int(input('Digite um valor para ver seu Fatorial: '))
cont = n
f = 1
print(f'Calculando {n}!', end=' > ')
while cont > 0:
    print(f'{cont}', end='')
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= cont
    cont -= 1
print(f)
