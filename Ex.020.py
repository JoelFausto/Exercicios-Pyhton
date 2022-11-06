from random import shuffle
print('Oi! Robby aqui :P')
print('Diga o nome de quatro pessoas e sortear uma ordem nessa lista!')
p1 = str(input('Primeiro nome: '))
p2 = str(input('Segundo nome: '))
p3 = str(input('Terceiro nome: '))
p4 = str(input('Quarto nome: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem da lista sorteada foi: ')
# print(f'{random.sample(lista, k=len(lista))}')
print(lista)
