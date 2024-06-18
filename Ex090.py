dados = {}
for d in range(0, 1):
    dados['Nome'] = str(input('Nome: '))
    dados['Média'] = float(input(f'Média de {dados['Nome']}: '))
print()
if dados['Média'] >= 7:
    dados['Situação'] = 'APROVADO'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'RECUPERAÇÃO'
else:
    dados['Situação'] = 'REPROVADO'
for k, v in dados.items():
    print(f'{k}: {v}')
