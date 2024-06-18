from moeda_prof import *

v = float(input('Digite um valor: R$'))
print(f'A metade de {moeda(v)} é {moeda(metade(v))}')
print(f'O dobro de {moeda(v)} é {moeda(dobro(v))}')
print(f'Aumentando 10%, temos {moeda(aumentar(v, 10))}')
print(f'Diminuindo 15%, temos {moeda(diminuir(v, 15))}')