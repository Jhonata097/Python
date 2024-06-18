from random import randint
from time import sleep
cont = 0

while True:
    print('-' * 30)
    print('>>>>>>>ÍMPAR / PAR<<<<<<<')
    print('-' * 30)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Ímpar ou Par?'
                            '\n[I/P] >> ')).strip().upper()[0]
    print('-' * 30)
    n = int(input('Digite um valor: '))
    print('-' * 30)
    computador = randint(0, 10)
    total = n + computador
    print(f'Valor do computador: {computador}')
    print('-' * 30)
    print('JOGANDO...')
    print('-' * 30)
    sleep(2)
    print(f'Total jogado: {total}')
    if total % 2 == 0 and escolha == 'P':
        print('JOGADOR venceu!')
        cont += 1
    if total % 2 == 0 and escolha == 'I':
        print('COMPUTADOR venceu!')
        break
    if total % 2 == 1 and escolha == 'P':
        print('COMPUTADOR venceu!')
        break
    if total % 2 == 1 and escolha == 'I':
        print('JOGADOR venceu!')
        cont += 1

print('-' * 30)
print('FIM DE JOGO!'
      f'\nVocê venceu {cont} vez(es).')
print('-' * 30)
