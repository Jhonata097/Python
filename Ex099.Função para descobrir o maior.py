from time import sleep

def maior(* valores):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('')
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi o {maior}')


maior(3, 4, 6, 8, 10, 1, 11, 34, 5)
maior(3, 8, 10, 0)