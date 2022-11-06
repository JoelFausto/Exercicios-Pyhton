print('Hi! This is a Robby! :P')
print('Andei pesquisando sobre mudanças de temperaturas!')
print('Aqui no Brasil medimos a temperatura em °C mas nos EUA e Canadá é medido em °F')
print('Me diga a temperatura em Celsius (°C) para eu transforma-la em Fahrenheit (°F)!\n')
C = float(input('Informe a temperatura em °C: '))
F = (C * 9 / 5) + 32
print(f'A temperatura de {C}°C corresponde a {F}°F!')
