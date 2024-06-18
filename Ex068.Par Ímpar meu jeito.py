from random import choice, randint
from time import sleep

cont = 0
while True:
    computador = choice(['PAR', 'ÍMPAR'])
    sorteio = randint(0, 20)
    print('-'*35)
    print(f'Computador escolhe: {computador}')
    print('-'*35)
    jogador = int(input('Escolha sua jogada:'
                        '\n[1] PAR'
                        '\n[2] ÍMPAR'
                        '\n>>> '))
    print('JOGANDO...')
    sleep(2)
    print(f'Valor sorteado: {sorteio}')
    if sorteio % 2 == 0 and jogador == 1:
        print('Resultado: PAR'
              '\nJogador venceu')
        cont += 1
    if sorteio % 2 == 0 and jogador == 2:
        print('Resultado: PAR'
              '\nComputador venceu')
        break
    if sorteio % 2 == 1 and jogador == 1:
        print('Resultado: ÍMPAR'
              '\nComputador venceu')
        break
    if sorteio % 2 == 1 and jogador == 2:
        print('Resultado: ÍMPAR'
              '\nJogador venceu')
        cont += 1
print(f'\nFim de jogo...'
      f'\nVocê venceu {cont} vez(es).')
