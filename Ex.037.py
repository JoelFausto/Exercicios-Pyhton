print('Hi! Robby na área :P')
print('Vamos converter números!')
print(' ')
num = int(input('Digite um número: '))
print('''Escolha uma das bases de conversões:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção Inválida! Tente novamente.')
