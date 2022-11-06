from random import randint
print('\033[1m-=-' * 8)
print('VAMOS JOGAR \033[31mPAR\033[m \033[1mOU \033[1;34mÍMPAR\033[m')
print('\033[1m-=-' * 8, '\033[m')
cont = 0
while True:
    player = int(input('Diga um valor: '))
    pc = randint(1, 10)
    s = player + pc
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if s % 2 == 0:
        r = 'PAR'
    else:
        r = 'ÍMPAR'
    print('-' * 53)
    print(f'Você jogou {player} e o computador {pc}. Total de {s} DEU {r}!')
    print('-' * 53)
    if r == 'PAR' and op == 'P':
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-' * 8)
        cont += 1
    elif r == 'PAR' and op == 'I':
        print('VOCÊ PERDEU!')
        print('-=-' * 8)
        break
    elif r == 'ÍMPAR' and op == 'I':
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-' * 8)
        cont += 1
    elif r == 'ÍMPAR' and op == 'P':
        print('VOCÊ PERDEU!')
        print('-=-' * 8)
        break
print(f'\033[1;31mGAME OVER!\033[m Você venceu {cont} vezes!')
