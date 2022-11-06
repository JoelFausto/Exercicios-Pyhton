print('Oi! Robby na área :P')
print('Me diga uns valores, vamos criar uma lista!')
print('-=-' * 14)
valores = []
cont = 0
while True:
    cont += 1
    if cont == 1:
        n = int(input('Digite um valor: '))
        valores.append(n)
    else:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        while op not in 'SN':
            op = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()
        if op == 'S':
            n = int(input('Digite um valor: '))
            valores.append(n)
        else:
            break
print('-=-' * 15)
print(f'Foram digitados {len(valores)} elementos!')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
