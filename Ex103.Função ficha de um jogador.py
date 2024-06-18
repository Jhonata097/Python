def ficha(nome='<Desconhecido>', gols=0):
    print('-=' * 20)
    print('FICHA DO JOGADOR: ')
    print(f'Nome: {nome}')
    print(f'Gols marcados: {gols} gol(s)')


n = str(input('Nome do jogador: '))
g = str(input(f'Gols marcador por {n}: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)