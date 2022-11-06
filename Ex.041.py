from datetime import date
print('\033[1mConfederação Nacional de Natação - CLASSIFICAÇÃO\033[m')
print(' ')
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = abs(ano - nasc)
print(f'O atleta tem {idade} ano(s).')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
