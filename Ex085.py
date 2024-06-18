num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 20)
num[0].sort()
print(f'Números PAR(ES): {num[0]}')
num[1].sort()
print(f'Números ÍMPAR(ES): {num[1]}')
print('-=' * 20)
