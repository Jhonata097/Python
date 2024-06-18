i = int(input('Início: '))
r = int(input('Razão: '))
termo = i
cont = 1
while cont <= 10:
    print(f'{termo}', end=' ')
    termo += r
    cont += 1
