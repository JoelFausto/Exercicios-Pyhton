from random import choice
from time import sleep
print('Opá! Aqui é Robby :P')
print('Que tal jogarmos JOKENPÓ!?')
print(' ')
PC = choice(['PEDRA', 'PAPEL', 'TESOURA'])
Jogador = str(input('Qual é sua jogada? (Pedra/Papel/Tesoura) ')).strip().upper()
print(' ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÓ!')
print(' ')
if PC == Jogador:
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mEMPATE!\033[m')
elif PC == 'PEDRA' and Jogador == 'PAPEL':
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mJogador VENCEU!\033[m')
elif PC == 'PEDRA' and Jogador == 'TESOURA':
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mComputador VENCEU!\033[m')
elif PC == 'PAPEL' and Jogador == 'TESOURA':
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mJogador VENCEU!\033[m')
elif PC == 'PAPEL' and Jogador == 'PEDRA':
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mComputador VENCEU!\033[m')
elif PC == 'TESOURA' and Jogador == 'PEDRA':
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mJogador VENCEU!\033[m')
elif PC == 'TESOURA' and Jogador == 'PAPEL':
    print('-=-' * 17)
    print(f'Computador jogou {PC}')
    print(f'Jogador jogou {Jogador}')
    print('-=-' * 17)
    print('\033[1;34mComputador VENCEU!\033[m')
else:
    print('\033[1;031mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')
