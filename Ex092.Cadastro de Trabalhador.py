from datetime import datetime

trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = datetime.now().year - trabalhador['Nascimento']
trabalhador['Carteira de Trabalho'] = int(input('Carteira de Trabalho (Se não tem digite 0): '))
if trabalhador['Carteira de Trabalho'] != 0:
    trabalhador['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    aposentadoria = trabalhador['Idade'] + ((trabalhador['Ano de Contratação'] + 35) - datetime.now().year)
    trabalhador['Aposentadoria'] = aposentadoria
print('')
for k, v in trabalhador.items():
    print(f'{k}: {v}')
    