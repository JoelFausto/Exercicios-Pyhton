print('Opá! Robby por aqui :P')
print('Hoje quero multiplicar novamente! Me diga um número e eu lhe mostrarei sua tabuada!')
n = int(input('Digite um número para vermos sua tabuada: '))
print('-' * 12)
for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')
print('-' * 12)
