pesos = []
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    pesos.append(peso)
print(f'A pessoa mais pesada pesa {max(pesos)}Kg')
print(f'A pessoa mais leve pesa {min(pesos)}Kg')
