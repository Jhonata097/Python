def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaaumento=0, taxareducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço:  \t{moeda(dobro(preco))}')
    print(f'Metade do preço: \t{moeda(metade(preco))}')
    print(f'{taxaaumento}% de aumento: \t{moeda(aumentar(preco, taxaaumento))}')
    print(f'{taxareducao}% de redução: \t{moeda(diminuir(preco, taxareducao))}')
    print('-' * 30)


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)