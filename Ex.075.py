tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu pela primeira vez na {tupla.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valor(es) pare(s) digitado(s) foram: ', end='')
cont = 0
for n in tupla:
    if n % 2 == 0:
        cont += 1
        print(n, end=' ')
if cont == 0:
    print('\033[31mNão foram digitados números pares!\033[m')
