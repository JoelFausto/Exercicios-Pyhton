print('Oi! Aqui é o Robby :P')
print('Me diga seu nome completo para eu ver se tem Silva nele!')
nome = str(input('Digite seu nome completo: ')).strip().upper()
d = nome.split()
s = 'SILVA' in d
print(f'Tem Silva? {s}')
