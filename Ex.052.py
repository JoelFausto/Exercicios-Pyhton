print('Olá, aqui é o Robby :P')
print('Me diga um número e lhe direi se ele é PRIMO!')
num = int(input('Digite um número: '))
s = 0
for c in range(1, num + 1):
    if num % c == 0:
        s = s + 1
        print(f'\033[34m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisível {s} vezes.')
if s == 2:
    print('E por isso ele é \033[1;34mPRIMO!\033[m')
else:
    print('E por isso ele é \033[1;31mNÃO é PRIMO!\033[m')
