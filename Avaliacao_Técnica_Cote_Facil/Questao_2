import scrapy


class PedidosSpider(scrapy.Spider):
    name = 'pedido'

    def __init__(self, numero_pedido=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numero_pedido = numero_pedido

    def start_requests(self):
        yield scrapy.Request(
            url='https://pedidoeletronico.servimed.com.br/',
            callback=self.efetuar_login,
            dont_filter=True
        )

    def efetuar_login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'juliano@farmaprevonline.com.br', 'senha': 'a007299A'},
            callback=self.acessar_meus_pedidos,
            dont_filter=True
        )

    def acessar_meus_pedidos(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'pedido': self.numero_pedido},
            callback=self.obter_faturamento,
            dont_filter=True
        )

    def obter_faturamento(self, response):
        motivo = response.css('.alert.alert-info p::text').get().strip()
        itens = []
        for item in response.css('#items tbody tr'):
            codigo_produto = item.css('td:nth-child(1)::text').get().strip()
            descricao = item.css('td:nth-child(2)::text').get().strip()
            quantidade_faturada = item.css('td:nth-child(3)::text').get().strip()
            itens.append({
                'codigo_produto': codigo_produto,
                'descricao': descricao,
                'quantidade_faturada': quantidade_faturada
            })
        if motivo.startswith('Nenhum'):
            return {'erro': 'Pedido não encontrado.'}
        else:
            return {'motivo': motivo, 'itens': itens}
        
