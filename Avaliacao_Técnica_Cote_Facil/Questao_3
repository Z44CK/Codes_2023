import requests
import json

# faz o login na página
login_data = {
    "email": "leonardo@coopertotal.com.br",
    "senha": "1234"
}
response = requests.post("http://coopertotal.nc7i.com/login", data=login_data)

# obtém o cookie da sessão
session_cookie = response.cookies.get_dict()

# acessa a página de pedidos para obter o valor mínimo de faturamento
pedidos_url = "http://coopertotal.nc7i.com/pedidos"
pedidos_response = requests.get(pedidos_url, cookies=session_cookie)

valor_minimo_faturamento = 1000  # substituir pelo valor mínimo de faturamento obtido na página

# adiciona os itens no carrinho de compras
adicionar_item_url = "http://coopertotal.nc7i.com/pedido/adicionar-item"
itens = [
    {"codigo_barras": "7896241225530", "quantidade": 1},
    {"codigo_barras": "7897595901927", "quantidade": 2},
    {"codigo_barras": "7896241225547", "quantidade": 1}
]
total_pedido = 0

for item in itens:
    item_data = {
        "codigoBarras": item["codigo_barras"],
        "quantidade": item["quantidade"]
    }
    response = requests.post(adicionar_item_url, data=item_data, cookies=session_cookie)
    total_pedido += float(response.json()["valorTotal"].replace(",", "."))

# verifica se o valor mínimo de faturamento foi atingido
if total_pedido < valor_minimo_faturamento:
    # adiciona o produto 7896007547654 com a menor quantidade possível para atingir o valor mínimo de faturamento
    produto_adicional_data = {
        "codigoBarras": "7896007547654",
        "quantidade": int((valor_minimo_faturamento - total_pedido) / 5)  # substituir 5 pelo valor unitário do produto
    }
    response = requests.post(adicionar_item_url, data=produto_adicional_data, cookies=session_cookie)

# acessa a página de pedido para obter o status e o número do pedido
pedido_url = "http://coopertotal.nc7i.com/pedido"
pedido_response = requests.get(pedido_url, cookies=session_cookie)

status_pedido = pedido_response.json()["statusPedido"]
numero_pedido = pedido_response.json()["idPedido"]

# gera o JSON com o status e o número do pedido
pedido_json = {
    "status": status_pedido,
    "numero": numero_pedido
}
