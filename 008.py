# Codigo para criar uma lista em python, onde você insere, lista e deleta as informações.

import os

lista = []

while True:
    print('Slecione uma opção')
    opcao = str(input('[i]nserir: , [a]pagar: , [l]istar: '))

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice  para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um numero inteiro.')
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l')
