sal = float(input('Digite seu salário: R$'))

if sal > 1250:
    aumento = (sal * 0.1) + sal
    print(f'Aumento de 10%. Seu salário aumentará de R${sal:.2f} para R${aumento:.2f}')
else:
    aumento = (sal * 0.15) + sal
    print(f'Aumento de 15%. Seu salário aumentará de R${sal:.2f} para R${aumento:.2f}')
    