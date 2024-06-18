numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
opc = int(input('Qual número de 0 a 20 deseja ver por extenso?'
                '\n>> '))

while opc not in range(0, 21):
    opc = int(input('Tente novamente (0 a 20)'
                    '\n>> '))

print(f'Você digitou o número {numeros[opc]}')
