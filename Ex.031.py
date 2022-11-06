from time import sleep
print('Robby Travelers :P')
print('Vamos calcular o valor da sua viagem!')
distancia = float(input('Qual é a distância da sua viagem em KM? '))
print('PROCESSANDO...')
print(' ')
sleep(2)
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    valor = distancia * 0.50
    print(f'E o preço da sua passagem é R${valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'E o preço da sua passagem é R${valor:.2f}')
