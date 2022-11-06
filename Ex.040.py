print('\033[1mRobby Academy :P\033[m')
print('Vamos conferir seus status escolar!')
print(' ')
n1 = float(input('1VA: '))
n2 = float(input('2VA: '))
m = (n1 + n2) / 2
print(' ')
print(f'Tirando {n1} e {n2}, a média do discente é {m}')
if m >= 7:
    print(f'O discente está \033[1;033mAPROVADO!')
elif m < 5:
    print(f'O discente está \033[1;031mREPROVADO!')
elif 5 <= m < 7:
    print(f'O discente está em \033[1mRECUPERAÇÃO!')
