print('Oi! Aqui é o Robby :P')
op = 'S'
maior = menor = media = cont = 0
while op in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    media += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
print(f'Você digitou {cont} números, e a média entre eles é {media/cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
