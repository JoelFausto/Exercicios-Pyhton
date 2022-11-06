from random import choice
print('Oi! Robby aqui :P')
print('Diga o nome de quatro pessoas e irei sortear uma!')
p1 = str(input('Primeiro nome: '))
p2 = str(input('Segundo nome: '))
p3 = str(input('Terceiro nome: '))
p4 = str(input('Quarto nome: '))
lista = [p1, p2, p3, p4]
# Para fazer uma lista no Python basta colocar os elementos em colchetes!
print(f'O escolhido(a) foi {choice(lista)}')
