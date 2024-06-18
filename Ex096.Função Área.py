def area(larg, comp):
    print(f'A área de um terreno {larg} x {comp} é de {larg*comp}mª')


print('-' * 45)
print('              CONTROLE DE TERRENOS')
print('-' * 45)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
