print('\033[1m-' * 25)
print(" " * 5, "Robby Store's", " " * 5)
print('-' * 25, '\033[m')
total = totmil = barato = cont = 0
prdt = ''
while True:
    cont += 1
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço: R$'))
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1:
        barato = valor
        prdt = produto
    elif valor < barato:
        barato = valor
        prdt = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
    print(' ')
print(' ')
print('\033[1;34m-' * 17, 'FIM DO PROGRAMA', '-' * 17, '\033[m')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {prdt} que custa R${barato:.2f}')
print('\033[1;34m-' * 51)
