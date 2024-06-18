sexo = input('Digite seu sexo [M / F]: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Opção inválida. Digite M ou F: ').strip().upper()[0]
if sexo in 'Mm':
    print('Sexo MASCULINO registado')
if sexo in 'Ff':
    print('Sexo FEMININO registrado')
