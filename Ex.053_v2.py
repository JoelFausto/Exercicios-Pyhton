print('Olá! Robby na área :P')
print('Digite uma frase e vamos ver se ela é um Palíndromo!')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print("Temos um Palíndromo!")
else:
    print('A frase digitada NÃO é um Palíndromo!')
