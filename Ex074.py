from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Número randomizados: ', end='')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nMaior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')
