n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor (999 para encerrar): '))
    if n != 999:
        cont += 1
        soma += n
print(f'\nTotal de números digitados: {cont}')
print(f'Soma dos números digitados: {soma}')
