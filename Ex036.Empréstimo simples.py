print('>>>>>>>>>>>>>>>>BEM VINDO(A) AO BANCO ITACÚ<<<<<<<<<<<<<<<<')
print('Saia do aluguél! Simule seu empréstimo:')
val = float(input('Qual é valor do imóvel? R$'))
sal = float(input('Qual sua renda mensal? R$'))
anos = int(input('Em quanto tempo (anos) você pretende pagar? '))

pmensal = val / (anos * 12)
minimo = sal * 0.3

if pmensal <= minimo:
    print('\nEMPRÉSTIMO APROVADO!')
    print(f'O valor das prestações mensais é menor ou igual a 30% da sua renda:')
    print(f'R${pmensal:.2f} < R${minimo:.2f}')
    print(f'Você irá pagar {anos * 12} parcelas de R${pmensal:.2f}.')
else:
    print('\nEMPRÉSTIMO NEGADO!')
    print(f'O valor das prestações mensais é maior que 30% da sua renda:')
    print(f'R${pmensal:.2f} > R${minimo:.2f}')
