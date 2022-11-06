print('Oi! Aqui é o Robby :P')
print('Vamos comparar dois números!')
print(' ')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
if num1 > num2:
    print('O PRIMEIRO valor é MAIOR!')
elif num2 > num1:
    print('O SEGUNDO valor é MAIOR!')
elif num1 == num2 and num2 == num1:
    print('Não existe valor maior, os dois são IGUAIS!')
