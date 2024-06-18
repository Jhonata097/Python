print('-=-=-=-=-=-=-=-=-=-=-=-=-RADAR-=-=-=-=-=-=-=-=-=-=-=-=-\n')
print('VIA 80Km/h')
radar = int(input('Velocidade detectada (Km/h): '))
print(f'Velocidade registrada: {radar}Km/h')

if radar > 80:
    multa = (radar - 80) * 7
    print(f'Você foi MULTADO! Velocidade de 80Km/h excedida! \nValor da multa: R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança...')
