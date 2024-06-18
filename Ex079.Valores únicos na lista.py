numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado!')
    else:
        print('Número duplicado, não será adicionado!')
    sair = str(input('Quer continuar? [S/N]'
                     '\n>> ')).strip().upper()
    if sair in 'N':
        break

print('')
numeros.sort()
print(f'Lista criada em ordem crescente: {numeros}')
