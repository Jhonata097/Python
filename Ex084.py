dados = []
galera = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:  # Se ainda não há ninguém cadastrado
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    opc = str(input('Quer cadastrar mais pessoas? [S/N]'
                    '\n>> ')).strip().upper()[0]
    if opc in 'N':
        break

print('')
print(f'Ao todo, você cadastrou {len(galera)} pessoa(s)')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}')

