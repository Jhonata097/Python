produtos = ('Arroz', 35, 'Feijão', 14, 'Batata', 6, 'Macarrão', 4, 'Picanha do Lule', 40, 'Leite', 4.50)
print('-' * 40)
print('            LISTA DE PREÇOS')
print('-' * 40)

for p in range(0, len(produtos), 2):
    print(f'{produtos[p]:.<30}', end='')
    print(f'R${produtos[p+1]:>7.2f}')