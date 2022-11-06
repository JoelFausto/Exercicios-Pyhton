print("$ Robby Bank's $")
print("Preencha os campos abaixo para vermos se você poderá fazer um empréstimo!")
print(' ')
vlr = float(input('Valor da casa: R$'))
slr = float(input('Seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
prst = vlr / (anos * 12)
print(f'Para pagar uma casa de R${vlr:.2f}, em {anos} anos, a prestação será de R${prst:.2f}.')
if prst >= (slr * 30 / 100):
    print('Empréstimo \033[031mNEGADO!')
else:
    print('Empréstimo pode ser \033[032mCONCEDIDO!')
