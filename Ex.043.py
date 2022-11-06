print('=' * 12)
print('\033[1mCálculo IMC\033[m')
print('=' * 12)
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
IMC = peso / (altura * altura)
print(' ')
print(f'O seu IMC (Índice de Massa Corporal) é de {IMC:.1f}')
if IMC < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= IMC < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= IMC < 30:
    print("Você está com SOBREPESO!")
elif 30 <= IMC < 40:
    print('Você está com OBESIDADE!')
elif IMC >= 40:
    print('Você está com OBESIDADE MÓRBIDA!')
