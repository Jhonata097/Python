nome = str(input('Digite seu nome completo: ')).strip()  # Tira espaço de antes e depois

separa = nome.split()

print(f'{nome} em letras maiúsculas: {nome.upper()}')
print(f'{nome} em letras minúsculas: {nome.lower()}')
print(f'Quantas letras há ao todo (sem considerar os espaços): {len(nome.replace(' ', ''))}')
print(f'Seu primeiro nome {separa[0]} tem {len(separa[0])} letras')
