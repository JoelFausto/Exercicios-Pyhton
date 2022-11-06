print('\033[1m=' * 35)
print(' ' * 5, 'Sequência de Fibonacci')
print('=' * 35, '\033[m')
termos = int(input('Quantos termos você quer mostar? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
