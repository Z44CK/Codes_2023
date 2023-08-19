def calcula_juros(principal, taxa, tempo):
    juros = principal * taxa * tempo
    return juros


def calcular_parcelas(total_divida, parcelas):
    valor_parcelas = total_divida / parcelas
    return valor_parcelas


def main():
    divida = float(input('Informe o valor da divida: '))
    print('\n Tabela de parcelas')
    print('{:<20} {:<20} {:<20} {:<20}'.format('Valor da Divida', 'Valor dos Juros', 'Quantidade Parcelas', 'Valor da '
                                                                                                            'Parcela'))

    for parcelas, taxa in [(1, 0), (3, 0.10), (6, 0.15), (9, 0.20), (12, 0.25)]:
        juros = calcula_juros(divida, taxa, parcelas)
        total_divida = divida + taxa
        valor_parcelas = calcular_parcelas(total_divida, parcelas)

        print('{:<20} {:<20} {:<20} {:<20}'.format(total_divida, juros, parcelas, valor_parcelas))


if __name__ == '__main__':
    main()
