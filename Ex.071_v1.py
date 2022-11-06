print('\033[1m=' * 36, '\033[m')
print(' ' * 10, "\033[1;33mRobby Bank's $\033[m", '' * 10)
print('\033[1m=' * 36, '\033[m')
valor = float(input('Qual valor você quer sacar sacar? R$'))
cinq = vinte = dez = um = 0
print('\033[1m=' * 36, '\033[m')
while True:
    if valor % 50 == 0:
        cinq = valor / 50
        print(f"Total de {cinq:.0f} cédulas de R$50")
        break
    else:
        cinq = valor // 50
        valor = valor % 50
        print(f"Total de {cinq:.0f} cédulas de R$50")
    if valor % 20 == 0:
        vinte = valor / 20
        print(f"Total de {vinte:.0f} cédulas de R$20")
        break
    else:
        vinte = valor // 20
        valor = valor % 20
        print(f"Total de {vinte:.0f} cédulas de R$20")
    if valor % 10 == 0:
        dez = valor / 10
        print(f"Total de {dez:.0f} cédulas de R$10")
        break
    else:
        dez = valor // 10
        valor = valor % 10
        print(f"Total de {dez:.0f} cédulas de R$10")
    if valor % 1 == 0:
        um = valor / 1
        print(f"Total de {um:.0f} cédulas de R$1")
        break
    else:
        um = valor // 1
        valor = valor % 1
        print(f"Total de {um:.0f} cédulas de R$1")
print('\033[1m=' * 36, '\033[m')
