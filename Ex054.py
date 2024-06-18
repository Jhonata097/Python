from datetime import date
anoatual = date.today().year

menor = 0
maior = 0

for i in range(1, 8):
    ano = int(input(f'Data de nascimento da {i}ª pessoa: : '))
    idade = anoatual - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'\nHá {maior} pessoa(s) com 18 anos ou mais.')
print(f'Há {menor} pessoa(s) com menos de 18 anos.')
