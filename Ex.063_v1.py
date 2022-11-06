print('\033[1m=' * 35)
print(' ' * 5, 'Sequência de Fibonacci')
print('=' * 35, '\033[m')
termos = int(input('Quantos termos você quer mostar? '))
cont = 1
t1 = 0
t2 = 1
while cont <= termos:
    print(f'{t1}', end='')
    print(' → ' if cont != termos else ' → FIM', end='')
    t3 = t1 + t2
    t2 = t1
    t1 = t3
    cont += 1
