# Faça um programa que peça 10 números inteiros, calcule e mostre
# a quantidade de números pares e a quantidade de números impares

# Solução com laço FOR:

par = 0
impar = 0
for i in range(10):
    num = int(input('Informe quma sequencia de dez numeros: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print('Quantidade de numeros pares é: ', par)
print('Quantidade de numreos impares é: ', impar)

-----------------------------------------------------------------------------------------------------

# Solução com WHILE:

num = input('Informe dez numeros inteiro separados por espaço: ').split()
pares = 0
impares = 0
i = 0

while i < len(num):
    if int(num[i]) % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1

print('Quantidade de numeros pares!', pares)
print('Quantidade de numeros impares!', impares)
