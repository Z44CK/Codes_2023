# Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
while True:
    try:
        a = float(input('Informe a quantidade populacional do pais A: '))
        b = float(input('Informe a quantidade populacional do pais B: '))
        n1 = float(input('Informe a taxa de crescimento do pais A (em porcentagem):'))
        n2 = float(input('Informe a taxa de crescimento do pais B (em porcentagem): '))

        if a <= 0 or b <= 0 or n1 <= 0 or n2 <= 0:
            raise ValueError("As populações e as taxas de crescimento devem ser valores positivos.")
        ano = 0

        print(f'População atual do pais A: {a:.2f}')
        print(f'População atual do pais B: {b:.2f}')

        while a <= b:
            a += a * (n1 / 100)
            b += b * (n2 / 100)
            ano += 1

        print(f'O pais A com a taxa de crescimento de {n1} levara {ano} anos para ultrapassar a população '
              f'do pais B com a taxa de crescimento de {n2}!')
        novamente = input('Deseja repetir a ação (S/N): ')
        if novamente.upper() != 'S':
            break
    except ValueError as e:
        print(f'Erro: {e}. Por Favor, insira um valores validos!')
