alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso (Kg): '))

imc = peso / alt ** 2

print(f'Seu IMC atual é {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Você está com peso IDEAL.')
elif imc >= 25 and imc <= 29.9:
    print('Você está com SOBREPESO.')
elif imc >= 30 and imc <= 39.9:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE EXTREMA.')
