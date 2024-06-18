lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    opc = str(input('Quer continuar? [S/N]'
                    '\n>> ')).strip().upper()
    if opc in 'Nn':
        break

print('')
print(f'Lista criada: {lista}')
print(f'Quantidade de elementos: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 aparece na galera!')
else:
    print('O número 5 não aparece na galera!')