# 1)
n = input('Informe seu nome completo: ')
print(n)

# --------------------------------------------------------------------------
# 2)
a = 5
b = 3
soma = a * b
print(soma)

# ---------------------------------------------------------------------------
# 3)
a = 5
b = 3
c = 5
soma = (a + b + c)
print(soma)

# --------------------------------------------------------------------------
# 4)

while True:
    n1 = input('Informe o numero: ')
    operador = input('Operador: ')
    n2 = input('Informe o numero: ')

    n1 = int(n1)
    n2 = int(n2)
    if operador == '+':
        print(n1+n2)
        break
    elif operador == '-':
        print(n1-n2)
        break
    elif operador == '*':
        print(n1*n2)
        break
    elif operador == '/':
        print(f'{n1/n2:.2f}')
        break
    else:
        print('Operador Inválido!')

# ------------------------------------------------------------------------
# 5)

contador = 1

while contador <= 10:
    print(contador)
    contador += 1
print('')
contador = 0

for contador in range(1, 11):
    print(contador)

# -------------------------------------------------------------------------
# 6)

pares = 0
impares = 0
num = 1
while num <= 10:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num += 1

print('Quantidade de números pares é:', pares)
print('Quantidade de números impares é:', impares)

print('')

# ---------------------------------------------------------------------------
# 7)

pares = 0
impares = 0

for num in range(1, 10):
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print('Quantidade de números pares é:', pares)
print('Quantidade de números impares é:', impares)

# -----------------------------------------------------------------------------------------------------
# 8)

a = float(input('Informe um valor: '))
b = float(input('Informe um valor: '))
c = float(input('Informe um valor: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('Não possui raizes reais!')
elif delta == 0:
    raiz = -b / (2*a)
    print('A raiz da equanção é:', raiz)
else:
    raiz1 = (-b+(delta ** 0.5)) / (2*a)
    raiz2 = (-b-(delta ** 0.5)) / (2*a)
    print('As raizes da equação são:', raiz1, 'e', raiz2)

# -----------------------------------------------------------------------
# 9)

import math

a = float(input('Informe um valor: '))
b = float(input('Informe um valor: '))
c = float(input('Informe um valor: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('Não possui raizes real!')
elif delta == 0:
    raiz = -b / (2*a)
    print('A raiz da equação é:', raiz)
else:
    raiz1 = (-b+(math.sqrt(delta)) / (2*a))
    raiz2 = (-b-(math.sqrt(delta)) / (2*a))
    print('As raizes da equação são:', raiz1, 'e', raiz2)

# ------------------------------------------------------------------------------------
# 10)

import math


def bhaskara(a, b, c):
    delta = b**2 - a*a*c
    if delta < 0:
        return None
    else:
        raizes = []
        m1 = math.sqrt(delta)
        r1 = (-b+m1) / (2*a)
        raizes.append(r1)
        r2 = (-b-m1) / (2*a)
        raizes.append(r2)
        return raizes


resultado = bhaskara(1, -5, 6)

if resultado is None:
    print('Não tem raizes reais para a equação.')
else:
    print(f'As raizes da equação são {resultado}.')


# --------------------------------------------------------------------------
# Responda as questões a seguir:
# O que significam palavras reservadas em python, e quais são eslas no código acima?

As palavras reservadas em python são aquelas que tem significado expecial para a linguagem, e portanto
não podem ser usadas como nomes de variaveis, classes, funções e as palavras reservadas do codigo acima são
if, else, def, return

# Qual a função de cada palavra reservada nesse código?
def -> define uma função, return -> ela retorna o resultado da função de volta ao seu chamador.
if e else -> são  estruturas de condição, como se fosse uma bifurcação, decidindo os blocos a serem executados
do programa sem executalos todos de uma só vez para decidiar qual caminho o programa vai seguir.
import -> importa pacotes ja programados e esta disponibilizados, e tambem serve para importar informações de
outros codigos python dentro da mesma pasta.

# Implemente a função acima e mostre na tela, o resultado da equação do segundo grau?
As raizes da equação são [4.6794494717703365, 0.320550528229663]

s = 'Mentorama'
s_upper = s.upper()

s_invertida = s_upper[:: -1]
print(s_invertida)

vogais = 'aeiou'.upper()
vogais_encontrada = ''
for letra in s_invertida:
    if letra in vogais:
        vogais_encontrada += letra
print(vogais_encontrada)

# ---------------------------------------------------------------------------------------
# 11)

import phonenumbers


nome = 'João'
sob = 'da Silva'
idade = '25'
cidade = 'São Paulo'
telefone = '1133333333'

telefone_ajustado = phonenumbers.parse(telefone, 'BR')
telefone = phonenumbers.format_number(telefone_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)

print('Nome:', nome + ' ' + sob)
print('Telefone:', telefone)
print('Idade:', idade)
print('Cidade:', cidade)

