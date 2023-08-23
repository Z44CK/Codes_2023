# Verifica a somatoria dos 2 inputs, caos sejam par/impar, positivo/negativo, inteiro ou decimal...

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

op = input('Qual operação deseja realizar:' '\n a- par ou impar: '
            '\n b- positivo ou negativo: '
            '\n c- inteiro ou decimal: '
            '\n Escolha: ')

if op == 'a':
    print('par' if (n1 + n2) % 2 == 0 else 'impar')
elif op == 'b':
    print('negativo' if (n1 + n2) < 0 else 'positivo')
else:
    print('inteiro' if n1 == round(n1) and n2 == round(n2, 2) else 'decimal')
    
# O código abaixo está refatorado, de forma mais concisa

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

result = n1 + n2
op = input('Qual operação deseja realizar:' '\n a- par ou impar: '
           '\n b- positivo ou negativo: '
           '\n c- inteiro ou decimal: '
           '\n Escolha: ')

if op == 'a':
    print('par' if result % 2 == 0 else 'impar')
elif op == 'b':
    print('negativo' if result < 0 else 'positivo')
else:
    print('inteiro' if result == round(result) else 'decimal')
