print('Oi! Robby na área :P')
print('Me diga uns valores, vamos criar uma lista e depois dividi-la em itens de pares e ímpares!')
print('-=-' * 30)
valores = []
pares = []
impares = []
cont = 0
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)
print('-=-' * 15)
print(f"A lista completa de números é {valores}")
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
