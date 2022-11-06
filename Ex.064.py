print('Olá! Aqui é o Robby :P')
cont = n = s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        s += n
        cont += 1
    else:
        print(' ', '\n\033[1mPrograma Finalizado!\033[m', '\n ')
print(f'Você digitou {cont} números e a soma entre eles foi de {s}.')
