print('Olá! Robby na área :P')
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print(f'{sexo} é uma opção inválida! Tente novamente!')
    else:
        if sexo == 'M':
            print('Entendi! Você é do genêro MASCULINO!')
        if sexo == 'F':
            print('Entendi! Você é do genêro FEMININO!')
