print('Opá! Robby na área :P')
print('Me diga um número pode ser de 0 á 9999, que vou analisá-lo para você!')
num = int(input('Digite um número: '))
print(' ')
print(f'Analisando o número {num}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhar: {m}')
