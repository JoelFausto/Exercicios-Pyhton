print('Olá! Robby na área :P')
print('Me diga eu frase para eu analisá-la!')
frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A')+frase.count('À')+frase.count('Á')+frase.count('Ã')+frase.count('Â')
print(f'A letra A aparece {a} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}.')
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}.')
