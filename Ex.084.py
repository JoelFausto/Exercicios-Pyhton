pessoas = list()
dados = list()
maiorP = menorP = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0:
        menorP = maiorP = pessoas[1]
    else:
        if pessoas[1] > maiorP:
            maiorP = pessoas[1]
        if pessoas[1] < menorP:
            menorP = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('-=-' * 15)
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maiorP}Kg. Peso de ', end='')
for p in dados:
    if p[1] == maiorP:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorP}Kg. Peso de ', end='')
for p in dados:
    if p[1] == menorP:
        print(f'[{p[0]}] ', end='')
print()
