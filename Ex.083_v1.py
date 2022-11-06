lista = list(input('Digite uma expressão: '))
aberto = (lista.count('('))
fechado = (lista.count(')'))
if aberto == fechado:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
