# Desenvolva um Web Crawler para “navegar” pelas páginas da Wikipédia:

# - Escolha uma página da Wikipédia e realize a raspagem dos dados da página.
# - Imprima na tela a mensagem “Página principal: {Nome da página visitada}”
# - Busque no texto da página em que foi feita a raspagem todos os links que apontem para outras páginas da Wikipédia.
# - Faça uma nova raspagem para cada novo link capturado e imprima em cada um deles a mensagem “Página secundária: {Nome da página visitada}”.

import requests
from bs4 import BeautifulSoup
import re


def link_da_pagina_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Obtendo o nome da pagina principal
    pagina_principal = soup.title.text.strip()
    print(f'Pagina principal: {pagina_principal}')

    # Encontrando todos os links para outras páginas da Wikipédia
    links = soup.find_all('a', href=re.compile(r'^/wiki/'))

    for link in links:
        # Construindo a URL completa para a nova página
        nova_pagina_url = 'https://pt.wikipedia.org/wiki/Nintendo' + link['href']
        response = requests.get(nova_pagina_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Obtendo o nome da página secundária
        pagina_secundaria_title = soup.title.text.strip()
        print(f'Pagina secundaria: {pagina_secundaria_title}')

# URL da página da Wikipédia para iniciar a raspagem
wikipedia_url = 'https://pt.wikipedia.org/wiki/Sony'
link_da_pagina_wikipedia(wikipedia_url)
