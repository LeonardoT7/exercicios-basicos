#Usuário informa 2 números com casas decimais.
n1 = float (input('Digite o primeiro número: '))
n2 = float (input('Digite o segundo número: '))

#Estrutura condicional para validar o resultado da soma.
resposta = float(input(f'Informe o resultado da operação: {n1} + {n2} = '))
if resposta == n1 + n2:
    print('Você acertou! ')
else:
    print('Você errou! O resultado correto é: ', {n1 + n2})

#Estrutura condicional para validar o resultado da subtração.
resposta = float(input(f'Informe o resultado da operação: {n1} - {n2} = '))
if resposta == n1 - n2:
    print('Você acertou! ')
else:
    print('Você errou! O resultado correto é: ', {n1 - n2})

#Estrutura condicional para validar o resultado da multiplicação.
resposta = float(input(f'Informe o resultado da operação: {n1} * {n2} = 5'))
if resposta == n1 * n2:
    print('Você acertou! ')
else:
    print('Você errou! O resultado correto é: ', {n1 * n2})

#Estrutura condicional para validar o resultado da divisão.
resposta = float(input(f'Informe o resultado da operação: {n1} / {n2} = '))
if resposta == n1 / n2:
    print('Você acertou! ')
else:
    print('Você errou! O resultado correto é: ', {n1 / n2})