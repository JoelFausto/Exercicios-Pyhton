from math import hypot
print('Olá sou eu Robby :P')
print('E hoje estou com vontade de achar a hipotenusa de um triângulo retângulo!')
ctop = float(input('Comprimento do cateto oposto: '))
ctad = float(input('Comprimento do cateto adjascente: '))
hip = hypot(ctop, ctad)
print(f'O comprimento da hipotenusa é igual a {hip:.2f}')
