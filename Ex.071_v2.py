print('\033[1m=' * 36, '\033[m')
print(' ' * 10, "\033[1;33mRobby Bank's $\033[m", '' * 10)
print('\033[1m=' * 36, '\033[m')
valor = int(input('Qual valor você quer sacar sacar? R$'))
print('\033[1m=' * 36, '\033[m')
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\033[1m=' * 36, '\033[m')
print("Volte sempre ao Robby Bank's! Tenha um bom dia!")
