def leiaInt(msg: str):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaInt('Digite um número: ')
print('-=' * 25)
print(f'Você digitou o número {n}')
