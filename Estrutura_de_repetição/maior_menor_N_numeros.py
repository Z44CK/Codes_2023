menor_numero = float('inf')  # inicializa a variavel com um valor muito alto
maior_numero = float('-inf')  # inicializa a variavel com um valor muito baixo

# pede para o usuairo informar a quantidade de numeros
n = int(input('Informe a quantidade de numeros: '))
for i in range(n):
    numero = int(input('Digite um numero: '))

    if numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero

print(f'O maior numero é {maior_numero} e o menor numero é {menor_numero}')
