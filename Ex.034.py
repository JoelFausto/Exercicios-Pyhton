print('Robby Company :P')
print('=' * 17)
print('REAJUSTE SALARIAL')
print('=' * 17)
salario = float(input('Qual o salário do funcionário? R$'))
if salario >= 1250.0:
    a = (salario * 10 / 100) + salario
else:
    a = (salario * 15 / 100) + salario
print(f'Quem ganhava R${salario} passa a ganhar R${a:.2f} agora.')
