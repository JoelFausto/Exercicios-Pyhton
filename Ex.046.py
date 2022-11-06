import emoji
from time import sleep
print('Oi! Aqui é o Robby :P')
print('\033[1;33mÉ Véspera de Ano Novo!\033[m')
print('Vamos fazer a contagem regressiva! Para o show de fogos de artifícios!')
print(' ')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(' ')
print(emoji.emojize(':fireworks:' * 10, language='alias'))
print('\033[1;33mFELIZ ANO NOVO!!!')
