from random import randint
from time import sleep

print(' ' * 13, 'Hi! This is Robby :P')
print('-=-' * 17)
print('Vou pensar em um número de 0 a 10! Tente adivinhar!')
computador = randint(0, 10)
total = 1
print('-=-' * 17)
jogador = int(input('Em que número eu pensei? '))
while jogador != computador:
    if jogador < computador:
        total += 1
        print('Mais...Tente mais uma vez!')
        jogador = int(input('Em que número eu pensei? '))
    elif jogador > computador:
        total += 1
        print('Menos...Tente mais uma vez!')
        jogador = int(input('Em que número eu pensei? '))
print(' ')
sleep(1)
if total == 1:
    print('Wow! Você é bom! Me venceu de primeira! PARABÉNS!!!')
else:
    print(f'Você acertou! E me venceu com {total} tentativas! PARABÉNS!')
