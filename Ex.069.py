i = h = m = 0
while True:
    print('-' * 25)
    print(' ' * 2, 'CADASTRO UMA PESSOA', ' ' * 2)
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        i += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    print('-' * 24)
    op = ' '
    while op not in 'SsNn':
        op = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('=' * 5, 'FIM DO PROGRAMA', '=' * 5)
print(f'Total de pessoas com mais de 18: {i}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {m} mulheres com menos de 20 anos.')
