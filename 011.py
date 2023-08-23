clientes = {
    'cliente1': ['banana', 'melancia', 'maçã'],
    'cliente2': ['chocolate', 'pão', 'bolo', 'morango'],
    'cliente3': ['ovo', 'arroz', 'queijo', 'refrigerante', 'salgadinho']
}
# Itera sobre os clientes
for cliente, itens in clientes.items():
    print(f'Itens do {cliente}')
    # Itera sobre os itens de cada cliente
    for item in itens:
        print(item)
    print()  # Linha vazia entre os clientes
