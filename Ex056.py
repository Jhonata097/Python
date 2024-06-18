media = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0

for p in range(1, 3):
    n = str(input(f'Nome da {p}ª pessoa: ')).strip()
    s = str(input('Seu sexo (M / F): ')).strip().upper()
    ida = int(input('Sua idade: '))
    print('-' * 30)
    media += ida
    if p == 1 and s == 'M':  # Testa a primeira pessoa
        maioridadehomem = ida
        nomevelho = n
    if s == 'M' and ida > maioridadehomem:
        maioridadehomem = ida
        nomevelho = n
    if s == 'F' and ida < 20:
        mulher += 1

print(f'A média de idade é de {media / 2} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Há {mulher} mulher(es) com menos de 20 anos.')
