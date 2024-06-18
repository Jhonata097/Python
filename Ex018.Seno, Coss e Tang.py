import math

ang = int(input('Informe um ângulo: '))
rad = math.radians(ang)  # Primeiro transformar o ângulo em radiano
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O ângulo de {ang}º tem como SENO = {seno:.6f}, COSSENO = {cos:.6f} e TANGENTE = {tan:.6f}')
