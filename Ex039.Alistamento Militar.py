from datetime import date

print('>>>>>>>>>>>>>>>>ALISTAMENTO MILITAR<<<<<<<<<<<<<<<<')

atual = date.today().year
ano = int(input('Informe o ano em que nasceu: '))
alist = atual - ano

if alist < 18:
    print(f'Ainda não é o momento! \nVocê deverá aguardar mais {18 - alist} anos para se alistar.')
elif alist == 18:
    print('Fique atento! \nVocê deverá se alistar nesse ano!')
elif alist > 18:
    print(f'Prazo expirado! \nVocê deveria ter se alistado há {alist - 18} ano(s).')
