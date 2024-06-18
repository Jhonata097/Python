cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()

print(f'Sua cidade começa com "Santo"? {cidade[:5] == 'SANTO'}')
