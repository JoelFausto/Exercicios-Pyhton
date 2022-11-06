from random import randint
from time import sleep

print(' ' * 13, 'Hi! This is Robby :P')
print('-=-' * 17)
print('Vou pensar em um número de 0 a 5! Tente adivinhar!')
computador = randint(0, 5)
print('-=-' * 17)
jogador = int(input('Em que número eu pensei? '))
print(' ')
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'PARABÉNS VOCÊ CONSEGUIU ME VENCER!')
else:
    print(f'EU GANHEI! Eu pensei em {computador} não em {jogador}!')
