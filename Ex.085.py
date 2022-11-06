lista = [[], []]
for c in range(7):
    num = int(input(f'Digite o {c + 1}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('=-=' * 15)
print(f'Os valores dos pares digitados foram: {sorted(lista[0])}')
print(f'Os valores dos ímpares digitados foram: {sorted(lista[1])}')
