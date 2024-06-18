valores = []
maior = []
menor = []
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for p, v in enumerate(valores):
    if v == max(valores):
        maior.append(p)
    if v == min(valores):
        menor.append(p)

print('')
print(f'Lista criada: {valores}')
print(f'O maior valor foi o {max(valores)}, na posição {maior}')
print(f'O menor valor foi o {min(valores)}, na posição {menor}')