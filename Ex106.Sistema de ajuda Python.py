from time import sleep

c = ('\033[m',         # 0 - Sem cor
     '\033[0;40;41m',  # 1 - Vermelho
     '\033[0;40;42m',  # 2 - Verde
     '\033[0;40;43m',  # 3 - Amarelo
     '\033[0;40;44m',  # 4 - Azul
     '\033[0;40;45m',  # 5 - Roxo
     '\033[7;40m'      # 6 - Branco
     )


def ajuda(com):
    titulo(f'Acessando o manaul do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 5
    print(c[cor], end='')
    print('~' * tam)
    print(f'   {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)