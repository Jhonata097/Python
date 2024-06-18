n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi {media:.1f} \nstatus: REPROVADO.')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media:.1f} \nstatus: RECUPERAÇÃO.')
elif media >= 7:
    print(f'Sua média foi {media:.1f} \nstatus: APROVADO!')
