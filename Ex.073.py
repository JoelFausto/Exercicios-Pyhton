print('Oi! Sou o Robby :P')
print('Vamos falar sobre futebol!')
times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'Fluminense', 'Santos',
         'São Paulo', 'Flamengo', 'Botafogo', 'Avaí', 'Bragantino', 'Atlético-GO', 'Goiás', 'Ceará-SC', 'Coritiba',
         'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')
print('\033[1m=\033[m' * 220)
print(f'\033[1;32mLista de times do Brasileirão:\033[m {times}')
print('\033[1m=\033[m' * 220)
print(f'\033[1;33mOs cinco primeiros são:\033[m {times[:5]}')
print('\033[1m=\033[m' * 220)
print(f'\033[1;31mOs quatro últimos são:\033[m {times[-4:]}')
print('\033[1m=\033[m' * 220)
print(f'\033[1;32mTimes em ordem alfabética:\033[m {sorted(times)}')
print('\033[1m=\033[m' * 220)
if "Chapecoense" in times:
    print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição.')
else:
    print('A Chapecoense \033[1;31mnão está na lista!\033[m')
print('\033[1m=\033[m' * 220)
