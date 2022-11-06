print(' ' * 27, 'Hi! Robby in área :P')
print(' ' * 24, 'Vamos analisar triângulos!')
print('=' * 83)
print('Me diga o valor de três segmentos e lhe direi se podem ou não formar um triângulo!')
print('=' * 83)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
print(' ')
if s2 - s3 < s1 < s2 + s3 and s1 - s3 < s2 < s1 + s3 and s1 - s2 < s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO!')
    if s1 == s2 == s3:
        print('E será um TRIÂNGULO EQUILÁTERO!')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('E será um TRIÂNGULO ISÓSCELES!')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('E será um TRIÂNGULO ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO!')
