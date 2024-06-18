n = int(input('Digite um número: '))
total = n
cont = 1
maior = n
menor = n

while n != 9999999999999999999999999999:
    opc = input('Deja continuar? [S / N]: ').strip().upper()[0]
    if opc == 'S':
        n = int(input('Digite outro número: '))
        total += n
        cont += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    else:
        break

print(f'\nMédia dos números: {total/cont:.1f}')
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
