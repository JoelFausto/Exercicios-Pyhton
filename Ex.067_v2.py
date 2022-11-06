print('Opá! Robby por aqui :P')
print('Hoje quero multiplicar mais uma vez! Me diga um número e eu lhe mostrarei sua tabuada!')
print(' ')
while True:
    n = int(input('Digite um número para vermos sua tabuada: '))
    print('-' * 42)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 42)
print('\033[1;31mPROGRAMA TABUADA ENCERRADO! Volte sempre!\033[m')
