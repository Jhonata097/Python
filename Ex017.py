import math

cato = float(input('Informe o comprimento do cateto oposto: '))
cata = float(input('Informe o comprimento do cateto adjacente: '))
hip = math.hypot(cato, cata)
print(f'A hipotenusa desse triângulo é igual a {hip:.2f}')
