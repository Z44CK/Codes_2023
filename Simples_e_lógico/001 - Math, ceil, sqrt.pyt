from math import ceil, sqrt

num = int(input('Informe um numero: '))
print(f'A raiz quadrada de {num:.2f} é: {sqrt(num):.2f}')
print(f'O numero {num} arredondado para cima fica: {ceil(sqrt(num)):.2f}')
