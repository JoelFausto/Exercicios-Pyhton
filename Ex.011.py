print('Oi! Aqui é o Robby :P')
print('Que tal me dizer a altura e largura da sua parede!')
print('Com isso poderei lhe dizer quanto de tinta será necessário para pintá-la.\n')
largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'E com isso, para pintar essa parede, você precisará de {area / 2}l de tinta!')
