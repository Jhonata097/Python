from datetime import date

print('-=' * 20)
print('   CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=' * 20)

atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano

if idade <= 9:
    print(f'Você tem {idade} anos. Sua classe é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos. Sua classe é INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos. Sua classe é JUNIOR.')
elif idade <= 25:
    print(f'Você tem {idade} anos. Sua classe é SÊNIOR.')
elif idade >= 26:
    print(f'Você tem {idade} anos. Sua classe é MASTER.')
