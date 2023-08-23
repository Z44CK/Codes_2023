# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades


n = int(input('Informe um valor inteiro menor que 1000: '))

result = ' '
num = n
if n >= 100:
    centenas = n // 100
    if centenas > 1:
        result += f'{centenas} Centenas,'
    else:
        result += f'{centenas} Centena,'
    n = n % 100
    if n >= 10:
        dezenas = n // 10
        if dezenas > 1:
            result += f'{dezenas} Dezenas e '
        else:
            result += f'{dezenas} Dezena,'
unidades = n
if n > 10:
    result += f'{unidades} Unidade'
else:
    result += f'{unidades} Unidade'

print(f'O numero {num} é composto por{result}.')
