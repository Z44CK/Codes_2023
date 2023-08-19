# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B
# mantidas as taxas de crescimento informadas pelo usuário.
# Permita o usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    populacao_a = int(input('Informe a população do país A: '))
    populacao_b = int(input('Informe a população do país B: '))
    taxa_crescimento_a = float(input('Informe a taxa de porcentagem do país A: '))
    taxa_crescimento_b = float(input('Informe a taxa de porcentagem do país B: '))

    a = 1 + taxa_crescimento_a / 100
    b = 1 + taxa_crescimento_b / 100

    anos = 0

    while populacao_a <= populacao_b:
        populacao_a *= a
        populacao_b *= b
        anos += 1

    print(f'Em {anos} anos, a população do país A ({populacao_a:.0f}) '
          f'ultrapassará ou igualará a população do país B ({populacao_b:.0f})')

    repetir = input('Deseja repetir a operação: (s/n) ')
    if repetir.lower() != 's':
        print('Programa encerrado!!')
        break
