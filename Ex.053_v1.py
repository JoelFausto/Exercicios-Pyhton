print('Olá! Robby na área :P')
print('Digite uma frase e vamos ver se ela é um Palíndromo!')
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
fraseI = frase[::-1]
print(f'O inverso de {frase} é {fraseI}')
if fraseI == frase:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada NÃO é um Palíndromo!')
