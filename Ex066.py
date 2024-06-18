cont = 0
soma = 0
while True:
    n = int(input('Digite um valor (999 para encerrar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} valores e sua soma foi {soma}.')
