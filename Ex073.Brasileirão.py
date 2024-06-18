tabela = ('Atlético-PR', 'Cruzeiro', 'Flamengo', 'Fortaleza', 'Vasco da Gama', 'Internacional', 'Palmeiras', 'Bragantino', 'Fluminense', 'Juventude',
          'Criciúma', 'Corinthians', 'Atlético-MG', 'Botafogo', 'Grêmio', 'São Paulo', 'Bahia', 'Atlético-GO', 'Vitória', 'Cuiabá')

print('TABELA DO BRASILEIRÃO 2024 - RODADA 1')
for pos, times in enumerate(tabela):
    print(f'{pos + 1:2} {times}')

print('\n')
print('Após a 1ª rodada...')
print(f'Os 5 primeiros colocados do Brasileirão são: {tabela[0:5]}')
print(f'Os 4 times na zona de rebaixamento são: {tabela[16:]}')
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print(f'O time do Flamengo está na {tabela.index('Flamengo') + 1}ª posição')
