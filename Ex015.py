print('>>>>>>>>>>ALUGUEL DE CARROS!<<<<<<<<<<')
d = int(input('Por quantos dias o carros foi alugado? '))
km = float(input('Quantos Km rodado(s)? '))
total = (d * 60) + (km * 0.15)
print(f'Total de dia(s): {d} dia(s). \nDistância percorrida: {km} Km. \nValor final: R${total:.2f}')
