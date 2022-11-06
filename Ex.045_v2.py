from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')
PC = randint(0, 2)
Jogador = int(input('Qual é a sua jogada? '))
print(' ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(' ')
print('-=-' * 10)
print(f'O computador jogou {itens[PC]}')
print(f'Jogador jogou {itens[Jogador]}')
print('-=-' * 10)
if PC == 0:
    if Jogador == 0:
        print('EMPATE!')
    elif Jogador == 1:
        print('JOGADOR VENCE!')
    elif Jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif PC == 1:
    if Jogador == 0:
        print('COMPUTADOR VENCE!')
    elif Jogador == 1:
        print('EMPATE!')
    elif Jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif PC == 2:
    if Jogador == 0:
        print('JOGADOR VENCE!')
    elif Jogador == 1:
        print('COMPUTADOR VENCE!')
    elif Jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
