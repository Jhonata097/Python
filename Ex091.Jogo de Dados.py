from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jhoninha'  : randint(1, 6),
        'Natanzera' : randint(1, 6),
        'Lukinhas'  : randint(1, 6),
        'Alex'      : randint(1, 6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'{k:<10} tirou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('')
print('>>>>>>>>>>>>>>RANKING<<<<<<<<<<<<<<')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}ª lugar: {v[0]:<10} com {v[1]} ponto(s)')