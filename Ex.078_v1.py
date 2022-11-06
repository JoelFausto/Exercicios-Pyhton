print('Opá! Aqui é o Robby :P')
print('Vamos criar uma lista de valores e encontrar seu maior e menor valor!')
print('-=-' * 23)
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('-=-' * 15)
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}, nas posições {valores.index(maior)}...')
print(f'O menor valor digitado foi {menor}, nas posições {valores.index(menor)}...')
