from test_fizzbuzz import verifica_multiplo


def main():
    try:
        n = int(input('Informe um numero: '))
        resultado = verifica_multiplo(n)
        print(resultado)

    except ValueError:
        print('Por favor, insira um numero natural valido!')


if __name__ == '__main__':
    main()
