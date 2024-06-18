matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):  # MONTAR A MATRIZ
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
print('-=' * 22)
for linha in range(0, 3):  # MOSTRAR A MATRIZ
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print('')
