print('Hi! This is Robby :P')
print('Vamos calcular o fatorial de um número!?')
n = int(input('Calcular o fatorial do número: '))
c = n
f = 1
if c == 0:
    print('Calculando 0! = 0')
print(f'Calculando {c}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
