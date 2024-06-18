lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    if n % 2 == 1:
        listaimpar.append(n)
    opc = str(input('Quer continuar? [S/N]'
                    '\n>> ')).strip().upper()[0]
    if opc in 'Nn':
        break

print('')
print(f'Lista: {lista}')
print(f'Lista de números Pares: {listapar}')
print(f'Lista de números Ímpares: {listaimpar}')

