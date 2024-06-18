while True:
    valor = int(input('Informe o valor a ser sacado : R$'))
    print('-' * 37)
    nota50 = valor // 50
    valor %= 50
    nota20 = valor // 20
    valor %= 20
    nota10 = valor // 10
    valor %= 10
    nota1 = valor // 1
    print(f'{nota50:2} nota(s) de R$50')
    print(f'{nota20:2} nota(s) de R$20')
    print(f'{nota10:2} nota(s) de R$10')
    print(f'{nota1:2} nota(s) de R$1')
    print('-' * 37)
    opc = str(input('Quer sacar um novo valor? '
                    '\nSim ou Não: >> ')).strip().upper()[0]
    print('-' * 37)
    if opc in 'Nn':
        print('Fim do programa...')
        break
