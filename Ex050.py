soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}ª número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Voce informou {cont} número(s) PAR(ES) e sua soma foi {soma}')
