import requests
import nacl.pwhash
import os
import json
from bs4 import BeautifulSoup

senha = b'85243140'

salt = os.urandom(16)

hash_senha = nacl.pwhash.argon2i.kdf(16, senha, salt)
with open('senha_segura.text', 'wb') as f:
    f.write(salt)
    f.write(hash_senha)

with requests.Session() as s:
    login_url = 'https://www.compra-agora.com/login'
    s.get(login_url)
    salt = s.cookies.get_dict()['PHPSESSID']
    csrf_input = BeautifulSoup(s.get(login_url).text, 'html.parser').find('input', {'name': '_csrf'})
    if csrf_input:
        csrf = csrf_input = ['value']

    hash_senha = (nacl.pwhash.argon2i.kdf(16, senha, salt))
    heanders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID={}'.format(salt),
        'Origin': 'https://www.compra-agora.com',
        'Referer': 'https://www.compra-agora.com/login',
    }
    data = {
        '_csrf': csrf,
        'usuário': '04.502.445/0001-20',
        'senha': hash_senha.hex()
    }
    s.post(login_url, headers=heanders, data=data)

    categorias = ['Alimentos', 'Bazar', 'Bebidas', 'Bomboniere', 'Cuidados Pessoais', 'Roupa e Casa']
    dados_produtos = []
for categoria in categorias:
    categoria_url = "https://www.compra-agora.com/{}/c".format(categoria)
    r = s.get(categoria_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    produtos = soup.find_all('div', class_='product_card')
    for produto in produtos:
        descricao = produto.find('div', class_='product_card_name').text.strip()
        fabricante = produto.find('div', class_='product_card_manufacturer').text.strip()
        img_url = produto.find("div", class_="product-card-image")['style'].replace("background-image: url"
                                                                                    "('", "").replace("');", "")
        dados_produtos.append({'descricao': descricao, 'fabricante': fabricante, 'img_url': img_url})

with open('dados_produtos.json', 'w') as f:
    json.dump(dados_produtos, f)
