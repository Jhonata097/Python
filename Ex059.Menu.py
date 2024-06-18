from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('-' * 34)
    print('               MENU')
    print('-' * 34)
    print('[1] SOMA\n'
          '[2] MULTIPLICAÇÃO\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR')
    print('-' * 34)
    opc = int(input('Digite a opção que deseja: '))
    if opc == 1:
        print(f'A soma entre {n1}+{n2} é {n1+n2}')
        sleep(2)
    elif opc == 2:
        print(f'A multiplicação entre {n1}x{n2} é {n1*n2}')
        sleep(2)
    elif opc == 3:
        print(f'O maior número entre {n1} e {n2} é {max(n1, n2)}')
        sleep(2)
    elif opc == 4:
        n1 = int(input('Digite o novo valor: '))
        n2 = int(input('Digite o novo valor: '))
        print(f'Novos valores registrados: {n1} e {n2}')
        sleep(2)
    elif opc == 5:
        print('Finalizando...')
        sleep(2)
        print('\nFim do programa!')
    else:
        print('Opção inválida! Tente novamente')
        sleep(2)


