from random import randint
from time import sleep

sorteio = randint(0, 5)

adv = int(input('O computador irá sortear um número aleatório entre 0 a 5. Coloque seu palpite: '))

print('SORTEANDO...')
sleep(2)
print(f'Seu palpite: {adv}. Número sorteado: {sorteio}.')

if sorteio == adv:
    print('Você adivinhou o número!! PARABÉNS!!')
else:
    print('Não foi dessa vez... Tente novamente!')
