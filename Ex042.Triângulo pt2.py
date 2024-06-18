print('-=' * 20)
print('        ANALISADOR DE TRIÂNGULO')
print('-=' * 20)
print('A seguir, informe três retas para criação de um TRIÂNGULO:')

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas informadas formam um triângulo ', end='')
    if r1 != r2 and r1 != r3 and r2 != r3:   # Retas diferentes
        print('ESCALENO.')
    elif r1 == r2 and r1 == r3 and r2 == r3:  # Retas iguais
        print('EQUILÁTERO.')
    else:
        print('ISÓSCELES.')
else:
    print('As retas informadas não formam um triângulo.')
