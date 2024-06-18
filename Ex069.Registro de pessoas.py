maior = 0
homem = 0
mulhermenos20 = 0

while True:
    print('=-' * 12)
    print('  REGISTRO DE PESSOAS')
    print('=-' * 12)
    i = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if i >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and i < 20:
        mulhermenos20 += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] > ')).strip().upper()[0]
    if opc == 'N':
        break

print(f'\nTotal de pessoa(s) maior(es) de idade: {maior}')
print(f'Total de homens: {homem}')
print(f'Total de mulheres com menos de 20 anos: {mulhermenos20}')
