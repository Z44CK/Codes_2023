menor = float('inf')  #lembre-se sempre inicializa a variavel com o maior valor
maior = float('-inf')  #lembre-se sempre incializa a variavel com o menor valor

n = int(input('Informe a quantidade de numeros entre 0 a 1000: '))
if n > 1000:
    print('Valor incorreto, insira um valor abaixo de mil!')
elif n < 0:
    print('Valor incorreto, insira um valor igual ou maior que zero!')
else:
    for _ in range(n):
        numero = int(input('Informe um numero: '))

        if numero < 0 or numero > 1000:
            print('Numero fora do intervalo permitido (0 a 1000).')
            break
        else:
            if numero > maior:
                maior = numero
            elif numero < menor:
                menor = numero

if menor == float('inf') or maior == float('-inf'):
    print('Nenhum numero valido foi inserido!')
else:
    print(f'O maior numero é {maior} e o menor numero é {menor}')
