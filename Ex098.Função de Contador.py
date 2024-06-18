from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 18)
    print(f'Contagem de {inicio} até {fim}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont += passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 18)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
print('-=' * 18)
