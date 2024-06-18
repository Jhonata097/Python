from moeda_prof import *

v = float(input('Digite um valor: R$'))
print(f'A metade de R${v} é R${metade(v)}')
print(f'O dobro de R${v} é R${dobro(v)}')
print(f'Aumentando 10%, temos R${aumentar(v, 10)}')
print(f'Diminuindo 15%, temos R${diminuir(v, 15)}')