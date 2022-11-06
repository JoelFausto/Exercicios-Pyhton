print('=' * 15)
print("\033[1m Robby Store's\033[m")
print('=' * 15)
valor = float(input('Preço das compras: R$'))
print(' ')
print('''\033[1mFORMAS DE PAGAMENTO\033[m
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual opção de pagamento? '))
if op == 1:
    desconto = abs((valor * 10 / 100) - valor)
    print(f'Sua compra de R${valor:.2f}, vai custar R${desconto:.2f} no final.')
elif op == 2:
    desconto = abs((valor * 5 / 100) - valor)
    print(f'Sua compra de R${valor:.2f}, vai custar R${desconto:.2f} no final.')
elif op == 3:
    print(f'Sua compra será parcelada em 2x de R${valor / 2:.2f}')
    print(f'Sua compra de R${valor:.2f}, vai custar R${valor:.2f} no final.')
elif op == 4:
    valorfinal = abs((valor * 20 / 100) + valor)
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${valorfinal / parcelas:.2f} COM JUROS!')
    print(f'Sua compra de R${valor:.2f}, vai custar R${valorfinal:.2f} no final.')
else:
    valor = 0
    print('\033[1;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[1m')
