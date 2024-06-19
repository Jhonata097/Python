opc = str
soma = 0
while opc != 'N':
    valor = float(input('Valor do produto: R$'))
    soma += valor
    while True:
        opc = str(input('Quer continuar? [S/N]'
                        '\n>> ')).strip().upper()[0]
        if opc in 'NS':
            break
        else:
            print('Erro! Digite S ou N.')
    if opc == 'N':
        break

print('*' * 40)
print(f'Soma do valor: R${soma:.2f}')
pago = float(input('Valor pago: R$'))
print('*' * 40)

troco = pago - soma
falta = soma - pago

if troco > 0:
    print(f'Total: R${soma:.2f}, Valor Pago {pago:.2f} -> Troco R${troco:.2f}')
elif troco < 0:
    print(f'Total: R${soma:.2f}, Valor Pago R${pago:.2f} -> Falta(m) R${falta:.2f}')
else:
    print(f'Total: R${soma:.2f}, Valor Pago R${pago:.2f} -> Pagamento Completo')


