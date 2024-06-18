from time import sleep
import emoji

print('CONTAGEM REGRESSIVA')
for i in range(10, -1, -1):  # De 10 a 0
    sleep(1)
    print(i)
print(emoji.emojize(':collision::collision:BOOOOOM:collision::collision:'))
