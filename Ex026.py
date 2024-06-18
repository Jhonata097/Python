frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Analisando a frase: {frase} ...')
print(f'Quantas vezes aparece a letra A? {frase.count('A')}')
print(f'Em que posição a letra A aparece a primeira vez? {frase.find('A') + 1}')  # Para ficar mais bonitinho
print(f'Em que posição a letra A aparece pela última vez? {frase.rfind('A') + 1}')  # Para ficar mais bonitinho
