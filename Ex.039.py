from datetime import date
print('ALISTAMENTO MILITAR')
print(' ')
gen = str(input('Digite seu genêro (Masculino/Feminino): ')).strip().upper()
if gen == 'FEMININO':
    print('O Alistamento Militar não é obrigatório para mulhures.')
else:
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos, em {atual}.')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        print(f'Ainda faltam {18 - idade} ano(s) para o alistamento.')
        print(f'Seu alistamento será em {abs((18 - idade) + atual)}.')
    elif idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} ano(s).')
        print(f'Seu alistamento foi em {abs((idade - 18) - atual)}.')
