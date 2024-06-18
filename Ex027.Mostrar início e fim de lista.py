nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print(f'Analisando o nome {nome} ...')
print(f'Primeiro nome: {separa[0]}')
print(f'Último nome: {separa[-1]}')
