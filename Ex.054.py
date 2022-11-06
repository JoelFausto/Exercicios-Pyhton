from datetime import date
print('Olá, Robby na área :P')
print('Vamos analisar a MAIORIDADE de um grupo de pessoas!')
men = 0
mai = 0
ano = date.today().year
print(' ')
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = abs(ano - nasc)
    if idade >= 21:
        mai += 1
    else:
        men += 1
print(' ')
print(f'Ao todo tivemos {mai} pessoas maiores de idade!')
print(f'E também tivemos {men} pessoas menores de idade!')
