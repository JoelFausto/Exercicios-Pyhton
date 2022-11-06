print('=' * 15)
print(' GERADOR DE PA')
print('=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = int(input('Quantos termos deseja ver? '))
decimo = primeiro + termos * razao
pa = 0
print(' ')
while primeiro != decimo:
    print(f'{primeiro}', end=' → ')
    pa = primeiro + razao
    primeiro = pa
print('FIM!')
