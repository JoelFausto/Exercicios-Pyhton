print('=' * 15)
print(' GERADOR DE PA')
print('=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 0
d = 10
print(' ')
while cont <= d:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
    if cont == d:
        print('PAUSA')
        n = int(input('Quantos termos você quer mostrar a mais? '))
        if n == 0:
            d = 0
        else:
            d += n
print(f'\nProgressão finalizada com {cont} termos mostrados!')
