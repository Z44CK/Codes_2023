# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

print('Notas disponiveis são: 1, 5, 10, 50, 100 R$')
print('O valor minimo para saques é de 10 reais, e o maximo é de 600 reais')
valor = int(input('Valor do saque: '))
total = valor
cem = int(valor / 100)
valor = valor - (cem * 100)

cinquenta = int(valor / 50)
valor = valor - (cinquenta * 50)

dez = int(valor / 10)
valor = valor - (dez * 10)

cinco = int(valor / 5)
valor = valor - (cinco * 5)

um = valor

print('Q.Notas R$100,00 = ', cem)
print('Q.Notas R$50,00 = ', cinquenta)
print('Q.Notas R$10,00 = ', dez)
print('Q.Notas R$5,00 = ', cinco)
print('Q.Notas R$1,00 = ', um)

print(f'O valor do saque é de R${total}')
