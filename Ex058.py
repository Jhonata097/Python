from random import randint

print('     SORTEIO DE NÚMEROS')

ale = randint(0, 10)
palpite = int(input('Digite seu palpite (0 a 10): '))
cont = 1
print('-'*38)
print(f'Seu palpite: {palpite}')
print(f'Número sorteado: {ale}')
print('-'*38)

while palpite != ale:
    ale = randint(0, 10)
    palpite = int(input('Errou! Tente novamente (0 a 10): '))
    print('-' * 38)
    print(f'Seu palpite: {palpite}')
    print(f'Número sorteado: {ale}')
    print('-' * 38)
    cont += 1

print(f'\nParabéns! Você acertou na {cont}ª tentativa!')
