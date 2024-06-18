matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for linha in range(0, 3):  # MONTAR A MATRIZ
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
print('-=' * 22)
for linha in range(0, 3):  # MOSTRAR A MATRIZ
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print('')
print('-=' * 22)
print(f'Soma dos valores PARES é {somapar}')
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é o {maior}')
