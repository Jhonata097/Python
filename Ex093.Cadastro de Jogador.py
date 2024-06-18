jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador['Nome']} Jogou? '))
for cont in range(1, total+1):
    partidas.append(int(input(f'Gol(s) feito(s) na {cont}ª partida: ')))
jogador['Gols'] = partidas[:]     # Adicionei os gols no dicionário pela cópia da galera de partidas
jogador['Total'] = sum(partidas)  # Somei os gols e adicionei o total no dicionário
print('-=' * 26)
print(jogador)
print('-=' * 26)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 26)
print(f'O jogador {jogador['Nome']} jogou {total} partida(s) e:')
for i, v in enumerate(jogador['Gols']):
    print(f' ⭢ Na partida {i+1}, fez {v} gol(s)')
print(f' ⭢ Fez um total de {jogador['Total']} gol(s)')
print('-=' * 26)
