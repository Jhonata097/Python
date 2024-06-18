lista = []

for p in range(0, 5):
    n = int(input('Digite um número: '))
    if p == 0:
        lista.append(n)
    elif n > lista[-1]:  # Se o número for maior que o último elemento da galera
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1


print('')
print(f'Lista digitada em ordem crescente: {lista}')
