#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))

while n2 < n1:
    n1 = int(input('Digite o valor 1: '))
    n2 = int(input('Digite o valor 2: '))

else:
    for i in range(n1, n2 + 1):
        print(f'O intervalo entre {n1} e {n2} é {i}')

##################################################################################
#Código alterado!

n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))

while n2 < n1:
    n1 = int(input('Digite o valor 1: '))
    n2 = int(input('Digite o valor 2: '))

else:
    soma = 0
    for i in range(n1, n2 + 1, 1):
        soma += i
        print(f'O intervalo entre {n1} e {n2} é {i}')
    print('\nA soma dos numeros é:', soma)
