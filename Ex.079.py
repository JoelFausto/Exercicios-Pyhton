print('Oi! Robby na área :P')
print('Me diga uns valores, vou criar uma lista e deixa-la em ordem crescente!')
print('-=-' * 24)
valores = []
cont = 0
while True:
    cont += 1
    if cont == 1:
        v = int(input('Digite um valor: '))
        if v in valores:
            print('Valor duplicado! Não vou adicionar...')
        else:
            valores.append(v)
            print('Valor adicionado com sucesso...')
    else:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        while op not in 'SN':
            op = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()
        if op == 'S':
            v = int(input('Digite um valor: '))
            if v in valores:
                print('Valor duplicado! Não vou adicionar...')
            else:
                valores.append(v)
                print('Valor adicionado com sucesso...')
        else:
            break
print('-=-' * 15)
print(f'Você digitou os valores {sorted(valores)}')
