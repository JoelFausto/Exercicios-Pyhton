print('\033[1m=' * 5, 'ANALISANDO', '\033[m=' * 5)
print(' ')
totidade = 0
maiorM = 0
nomeM = ''
menorF = 0
totidadeF = 0
for c in range(1, 5):
    print('-' * 5, f'{c}° PESSOA', '-' * 5)
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totidade += idade
    if c == 1 and sexo in 'Mm':
        maiorM = idade
        nomeM = nome
    if sexo in 'Mm' and idade > maiorM:
        maiorM = idade
        nomeM = nome
    if sexo in 'Ff' and idade < 20:
        totidadeF += 1
    print(' ')
print('\033[1mAnalisando...\033[m')
print(f'A média de idade do grupo é de {totidade/4:.1f} anos.')
print(f'O homem mais velho do grupo tem {maiorM} e se chama {nomeM}.')
print(f'Ao todo são {totidadeF} mulheres com menos de 20 anos.')
