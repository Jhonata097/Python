from random import shuffle
from time import sleep

adv = int(input('JOKENPÔ...\n'
                'Digite 1 para PEDRA \n'
                'Digite 2 para PAPEL \n'
                'Digite 3 para TESOURA\n'
                '>>>> '))
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

lista = ['PEDRA', 'PAPEL', 'TESOURA']
shuffle(lista)   # Sorteio da galera
pc = (lista[0])  # Mostra o primeiro item sorteado

if adv == 1 and pc == 'PEDRA':
    print('\nVocê escolheu: PEDRA')
    print(f'Computador escolheu: {pc}')
    print('\nEMPATE! Ambos escolheram PEDRA.')
elif adv == 1 and pc == 'PAPEL':
    print('\nVocê escolheu: PEDRA')
    print(f'Computador escolheu: {pc}')
    print('\nCOMPUTADOR VENCEU!')
elif adv == 1 and pc == 'TESOURA':
    print('\nVocê escolheu: PEDRA')
    print(f'Computador escolheu: {pc}')
    print('\nVOCÊ VENCEU!')
elif adv == 2 and pc == 'PEDRA':
    print('\nVocê escolheu: PAPEL')
    print(f'Computador escolheu: {pc}')
    print('\nVOCÊ VENCEU!')
elif adv == 2 and pc == 'PAPEL':
    print('Você escolheu: PAPEL')
    print(f'Computador escolheu: {pc}')
    print('\nEMPATE! Ambos escolheram PAPEL.')
elif adv == 2 and pc == 'TESOURA':
    print('\nVocê escolheu: PAPEL')
    print(f'Computador escolheu: {pc}')
    print('\nCOMPUTADOR VENCEU!')
elif adv == 3 and pc == 'PEDRA':
    print('\nVocê escolheu: TESOURA')
    print(f'Computador escolheu: {pc}')
    print('\nCOMPUTADOR VENCEU')
elif adv == 3 and pc == 'PAPEL':
    print('\nVocê escolheu: TESOURA')
    print(f'Computador escolheu: {pc}')
    print('\nVOCÊ VENCEU!')
elif adv == 3 and pc == 'TESOURA':
    print('\nVocê escolheu: TESOURA')
    print(f'Computador escolheu: {pc}')
    print('\nEMPATE! Ambos escolheram TESOURA.')
else:
    print('\nEssa opção não existe!')
