i = int(input('Início: '))
r = int(input('Razão: '))
n = int(input('Quantos elementos vão ser exibidos? '))
f = i + (n - 1) * r
f = f + 1

for c in range(i, f, r):
    print(f'{c}', end=' ')
