print('=' * 15)
print(' GERADOR DE PA')
print('=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
print(' ')
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'\nProgressão finalizada com {total} termos mostrados!')
