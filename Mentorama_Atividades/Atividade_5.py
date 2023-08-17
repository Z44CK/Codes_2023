import math


def imprimir_mensagem(mensagem):
    print(mensagem)


def multiplicar_numero(x, y):

     return math.prod([x * y])


mensagens = input('Informe a mensagem: ')

num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

imprimir_mensagem(mensagens)

resultado = multiplicar_numero(num1, num2)
print('O resultado da multiplicacao e: ', resultado)
