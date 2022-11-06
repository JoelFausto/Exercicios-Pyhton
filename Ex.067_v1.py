print('Opá! Robby por aqui :P')
print('Hoje quero multiplicar mais uma vez! Me diga um número e eu lhe mostrarei sua tabuada!')
print(' ')
while True:
    n = int(input('Digite um número para vermos sua tabuada: '))
    print('-' * 42)
    cont = 0
    if n < 0:
        break
    while True:
        print(f'{n} x {cont:2} = {n * cont}')
        if cont >= 10:
            print('-' * 42)
            break
        cont += 1
print('\033[1;31mPROGRAMA TABUADA ENCERRADO! Volte sempre!\033[m')
