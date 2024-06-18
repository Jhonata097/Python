n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 41)
print(f'               TABUADA DO {n}')
print('-' * 41)

for i in range(1, 11):
    print(f'{n} x {i:2} = {n * i}')
print('-' * 41)
