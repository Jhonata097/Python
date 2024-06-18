num = (int(input('Digite o 1ª número: ')),
       int(input('Digite o 2ª número: ')),
       int(input('Digite o 3ª número: ')),
       int(input('Digite o 4ª número: ')))

print(f'\nVocê digitou: {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vez(es)')
if 9 not in num:
    print(f'O número 9 não foi digitado!')
if 3 in num:
    print(f'O número 3 apareceu primeiro na {num.index(3) + 1}ª posição')
if 3 not in num:
    print('O número 3 não foi digitado!')
print('Número(s) PAR(ES) digitado(s): ', end='')

for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
