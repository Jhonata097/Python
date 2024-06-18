r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

print('-=-=-=- ANALISADOR DE TRIÂNGULOS -=-=-=-')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas informadas formam um triângulo')
else:
    print('As retas informadas não formam um triângulo')