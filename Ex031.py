dis = float(input('Qual a distância da viajem em km? '))

if dis <= 200:
    passagem = dis * 0.50
    print(f'Total da viajem: R${passagem:.2f}')
else:
    passagem = dis * 0.45
    print(f'Total da viajem: R${passagem:.2f}')
