matriz = [[], [], []]
for l1 in range(3):
    num = int(input(f'Digite um valor para {[0, l1]}: '))
    matriz[0].append(num)
for l2 in range(3):
    num = int(input(f'Digite um valor para {[1, l2]}: '))
    matriz[1].append(num)
for l3 in range(3):
    num = int(input(f'Digite um valor para {[2, l3]}: '))
    matriz[2].append(num)
print('-=-' * 10)
for m in matriz:
    print(f'[{m[0]:^5}]', end='')
    print(f'[{m[1]:^5}]', end='')
    print(f'[{m[2]:^5}]')
