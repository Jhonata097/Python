pessoas = dict()
galera = list()
soma = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        else:
            print('Erro! Digite M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        opc = str(input('Quer continuar? [S/N]'
                        '\n>> ')).strip().upper()[0]
        if opc in 'NS':
            break
        else:
            print('Erro! Digite S ou N.')
    if opc == 'N':
        break

print('=-' * 25)
print(f'Ao todo, foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A média de idade do grupo é igual a {media:.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p['Nome']}', end=' ')
print('')
print('Pessoa(s) com idade acima da média: ')
for p in galera:
    if p['Idade'] > media:
        print(f'{p['Nome']} com {p['Idade']} anos')

