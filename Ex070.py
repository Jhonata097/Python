total = 0
maisdemil = 0
menor = 0
while True:
    n = str(input('Nome do produto: '))
    v = float(input('Valor do produto: R$'))
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    total += v
    if v > 1000:
        maisdemil += 1
    if opc == 'N':
        break

print(f'\nTotal gasto: R${total:.2f}')
print(f'{maisdemil} produto(s) custa(m) mais de R$1000')
