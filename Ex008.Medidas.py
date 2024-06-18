m = float(input('Digite uma distância em metros: '))
deci = m * 10
cm = m * 100
mm = m * 1000
deca = m / 10
he = m / 100
km = m / 1000
print(f'A distância de {m} metro(s) é igual a {deci:.0f} decímetro(s), {cm:.0f} centímetro(s) e {mm:.0f} milímetro(s).')
print(f'A distância de {m} metro(s) é igual a {deca:.2f} decâmetro(s), {he:.2f} hectômetro(s) e {km:.2f} quilômetro(s).')
