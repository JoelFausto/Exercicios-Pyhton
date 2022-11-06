print('Hellou! Aqui é o Robby :P')
print("Me diga 7 números e vamos ver o resultado da soma entre os pares!")
s = 0
cont = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você digitou {cont} número(s) PARES! E o resultado de sua soma foi de {s}!')
