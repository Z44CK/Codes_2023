def menus():
    menu = {
        100: {"nome": "Cachorro Quente", "preco": 1.20},
        101: {"nome": "Bauru Simples", "preco": 1.30},
        102: {"nome": 'Bauru com ovos', "preco": 1.50},
        103: {"nome": "Hamburger", "preco": 1.20},
        104: {"nome": "Cheeseburger", "preco": 1.30},
        105: {"nome": "Refrigerante", "preco": 1.00}
    }

    return menu


def exibir_menu():
    menu = menus()
    print('Menu de itens:')
    for codigo, item in menu.items():
        print(f'Codigo: {codigo} - Item: {item["nome"]} - Preco: R${item["preco"]:.2f}')


def sistema():
    total_pedido = 0
    itens_pedidos = []
    print()
    exibir_menu()
    print()
    while True:
        codigo = int(input('Digite o codigo de um pedido: (ou 0 para encerrar o pedido: '))
        if codigo == 0:
            print('Pedido encerrado!')
            break

        if codigo in menus():
            quantidade = int(input('Informe a quantidade: '))
            item = menus()[codigo]
            preco_item = item["preco"]
            valor_pagar = preco_item * quantidade

            print(f'O valor a pagar pelo item é: {valor_pagar:.2f}')

            total_pedido += valor_pagar
            itens_pedidos.append((item['nome'], codigo, quantidade))
        else:
            print('Codigo invalido, por favor insira um codigo valido!')

    for nome, codigo, quantiade in itens_pedidos:
        print(f'Item: {nome} - Codigo: {codigo} - Quantidade: {quantiade}')


sistema()
