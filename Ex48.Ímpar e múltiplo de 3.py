soma = 0
cont = 0

for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:  # ÍMPARES E MÚLTIPLOS DE 3
        soma += i
        cont += 1

print(f'A soma dos {cont} números ÍMPARES MÚLTIPLOS DE 3, entre 1 e 500, é igual a {soma}')
