jogador = dict()
partidas = list()
lista = list()
while True:
    partidas.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador['Nome']} Jogou? '))
    for cont in range(1, total+1):
        partidas.append(int(input(f'Gol(s) feito(s) na {cont}ª partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(jogador['Gols'])
    lista.append(jogador.copy())
    opc = str(input('Quer continuar? [S/N]'
                    '\n>> ')).strip().upper()[0]
    if opc == 'N':
        break
print('-=' * 26)
print('Cód  ', end='')
for i in jogador.keys():
    print(f'{i:<14}', end='')
print('')
print('-=' * 26)
for k, v in enumerate(lista):
    print(f'{k:>2}   ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')
print('-=' * 26)
while True:
    busca = int(input('Mostrar jogador de qual jogador? [999 para encerrar]'
                      '\n>> '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'Levantamento do jogador {lista[busca]['Nome']}:')
        for i, g in enumerate(lista[busca]['Gols']):
            print(f' ⭢ No jogo {i+1} fez {g} gol(s)')
        print('-=' * 26)

