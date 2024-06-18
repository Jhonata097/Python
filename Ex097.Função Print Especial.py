def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'{msg:^{t}}')
    print('~' * t)


escreva('Olá, mundo!')
escreva('As três Graças: A desGraça; A sem Graça; E a nem de Graça')
