num = int(input('Digite um número inteiro: '))
opc = int(input('Digite 1 para ver seu número em BINÁRIO\n'
                'Digite 2 para ver seu número em OCTAL\n'
                'Digite 3 para ver seu número em HEXADECIMAL\n'
                '>>>>> '))

if opc == 1:
    bi = bin(num)[2:]  # Para tirar os dois dígitos iniciais inúteis
    print(f'O número {num} em BINÁRIO é: {bi}')
elif opc == 2:
    octal = oct(num)[2:]  # Para tirar os dois dígitos iniciais inúteis
    print(f'O número {num} em OCTAL é: {octal}')
elif opc == 3:
    hexa = hex(num)[2:].upper()  # Para tirar os dois dígitos iniciais inúteis
    print(f'O número {num} em HEXADECIMAL é: {hexa}')
else:
    print('Opção inválida!')
