print('Olá! Robby na área :P')
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n < 0 or n > 20:
            print('Tente novamente.')
        else:
            print(f'Você digitou o número: {num[n]}')
            break
    print(' ')
    op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op not in 'SN':
        op = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()
    if op == 'N':
        print('PROGRAMA ENCERRADO!')
        break
