print('-=' * 33)
print('                         MERCADO DO RUIM')
print('-=' * 33)

valor = float(input('Digite o valor total de suas compras: R$'))
pgm = int(input('Como prefere pagar?\n'
                'Digite 1 para pagamento à vista no pix ou dinheiro (10% de DESCONTO)\n'
                'Digite 2 para pagamento via débito de cartão (5% de DESCONTO)\n'
                'Digite 3 para pagamento em 2x no cartão (SEM JUROS)\n'
                'Digite 4 para parcelar em 3x ou mais no cartão (20% de JUROS)\n'
                '>>>> '))
if pgm == 1:
    pgm1 = valor - (valor * 0.1)  # Pix ou cheque
    print(f'Desconto de 10% aplicado! \nValor de R${valor:.2f} passa a ser R${pgm1:.2f}')
elif pgm == 2:
    pgm2 = valor - (valor * 0.05)  # Débito
    print(f'Desconto de 5% aplicado! \nValor de R${valor:.2f} passa a ser R${pgm2:.2f}')
elif pgm == 3:
    print(f'Nenhum desconto ou juros aplicado! \nVocê irá pagar R${valor:.2f} parcelado em 2x R${valor / 2:.2f}')
elif pgm == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    pgm4 = valor + (valor * 0.2)  # 3x ou mais no cartão
    print(f'Juros de 20% aplicado! \nVocê irá pagar R${valor:.2f} parcelado em {parcelas}x de R${pgm4 / parcelas:.2f}\n'
          f'Valor final R${pgm4:.2f}')
else:
    print('Opção de pagamento inválida!')
