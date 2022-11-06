matriz = [[], [], []]
totpar = tot = 0
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
    print(f'[ {m[0]} ]', end='')
    print(f'[ {m[1]} ]', end='')
    print(f'[ {m[2]} ]')
    if m[0] % 2 == 0:
        totpar += m[0]
    elif m[1] % 2 == 0:
        totpar += m[1]
    elif m[2] % 2 == 0:
        totpar += m[2]
    elif m[0][2] or m[1][2] or m[2][2]:
        tot +=
print('-=-' * 10)
print(f'A soma dos valores pares é {totpar}')
print(f'A soma dos valores da terceira coluna é {}')
