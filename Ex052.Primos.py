n = int(input('Digite um número: '))
cont = 0

for i in range(1, n+1):
    if n % i == 0:
        print(f'{n} é múltiplo de {i}')
        cont += 1
if cont == 2:
    print(f'{n} é PRIMO')
else:
    print(f'{n} não é PRIMO')
