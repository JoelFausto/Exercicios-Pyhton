print('=' * 21)
print(' 10 TERMOS DE UMA PA')
print('=' * 21)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (11 - 1) * r
for c in range(p, d, r):
    print(f'{c}', end=' → ')
print('ACABOU!')
