ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opc = str(input('Quer continuar? [S/N]'
                    '\n>> ')).strip().upper()[0]
    if opc in 'N':
        break
print('>>>>>>>>>>>>>>>> FICHA DOS ALUNOS <<<<<<<<<<<<<<<<<')
for e, a in enumerate(ficha):
    print(f'Número {e} - Aluno(a): {a[0]:<10} - Média: {a[2]:.1f} ')
print('-' * 51)
while True:
    opc = int(input('Quer mostrar as notas de qual aluno?'
                    '\n(999 encerra) >>  '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} foram: {ficha[opc][1]}')
        print('-' * 51)


