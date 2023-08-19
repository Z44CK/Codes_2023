# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
divisao = 0
for i in range(5):
    x = int(input('Digite o valor: '))
    soma += x
    divisao = (soma / 5)

print('Soma dos valores é:', soma, 'E a divisão entre os valores é:', divisao)
