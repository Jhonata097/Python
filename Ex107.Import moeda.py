from moeda import *

num = float(input('Informe um valor R$ '))
opc = int(input('O que deseja fazer? '
                '\n[1] - Aumentar % '
                '\n[2] - Diminuir % '
                '\n[3] - Dobrar'
                '\n[4] - Ver a metade'
                '\n>> '))
if opc == 1:
    aum = float(input(f'Digite uma porcentagem de aumento: '))
    aumentar(num, aum)
    print(f'R${num:.2f} + {aum:.0f}% = R${aumentar(num, aum):.2f}')

if opc == 2:
    dim = float(input(f'Digite uma porcentagem de redução: '))
    diminuir(num, dim)
    print(f'R${num:.2f} - {dim:.0f}% = R${diminuir(num, dim):.2f}')

if opc == 3:
    print(f'O dobro de R${num:.2f} é R${dobrar(num):.2f}')

if opc == 4:
    print(f'A metade de R${num:.2f} é R${metade(num):.2f}')