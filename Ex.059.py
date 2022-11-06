from time import sleep
print('Oi! Aqui é o Robby :P')
print('Me diga, dois números e vamos fazer algumas coisas!')
print(' ')
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
op = 0
while op != 5:
    print('''\033[4mMenu de Opções\033[m
\033[1;34m[ 1 ] SOMAR\033[m
\033[1;35m[ 2 ] MULTIPLICAR\033[m
\033[1;36m[ 3 ] MAIOR\033[m
\033[1;32m[ 4 ] NOVOS NÚMEROS\033[m
\033[1;31m[ 5 ] SAIR DO PROGRAMA\033[m''')
    op = int(input('>>>>> Qual é a sua opção: '))
    if op == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação entre {n1} x {n2} é {n1 * n2}')
    elif op == 3:
        if n1 > n2 and n2 < n1:
            print(f'Entre {n1} e {n2} o MAIOR é {n1}')
        elif n1 == n2:
            print(f'Os números {n1} e {n2} são iguais não há MAIOR nesta situação!')
        else:
            print(f'Entre {n1} e {n2} o MAIOR é {n2}')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o 1° número: '))
        n2 = float(input('Digite o 2° número: '))
    elif op > 5 or op == 0:
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m Tente novamente!')
    print('-=-' * 10)
    sleep(2)
print('\033[1mFinalizando...')
sleep(1.5)
print('Programa Finalizado! Volte Sempre!\033[m')
print('-=-' * 10)
