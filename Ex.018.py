from math import radians, sin, cos, tan
print('Opa! Robby na área :P')
print('Basta me dizer um ângulo que lhe direi seu SENO, COSSENO e TANGENTE!')
ang = float(input('Digite um ângulo: '))
print(f'O ângulo de {ang} tem o SENO de {sin(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan(radians(ang)):.2f}')
