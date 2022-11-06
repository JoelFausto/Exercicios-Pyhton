print('Oi! Robby na área :P')
print('Vou lhe mostrar a soma entre todos os números ímpares e múltiplos de 3, no intervalo de 1 e 500!')
s = 0
i = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        i += 1
        s += c
print(f'Foram encontrados {i} números ímpares e múltiplos de 3! E o resultado é {s}!')
