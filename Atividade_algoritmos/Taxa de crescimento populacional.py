# Supondo que a população de um país A
# seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
# calcule e escreva o número de anos necessários para que a
# população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.
a = 80000
b = 200000
ano = 0

print(f'População do pais A: {a:.2f}')
print(f'População do pais B: {b:.2f}')

while a <= b:
    a += a * 0.03
    b += b * 0.015

    ano += 1

print(f'O pais A com a taxa de crescimento de 3% ao ano '
      f'levará {ano} anos para ultrapassar a população do pais B que possui a taxa de crescimento de '
      f'1.5% ao ano!')
