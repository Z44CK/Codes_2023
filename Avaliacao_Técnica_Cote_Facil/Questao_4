from selenium.webdriver import WebDriver as Chrome
import sys

# Recebe o nome da autora como argumento
autora = sys.argv[1]

# Configuração do driver do navegador
driver: Chrome = Chrome()

# Acessa a página principal
driver.get("http://quotes.toscrape.com/")

# Encontra o link para a página da autora e clica nele
link_autora = driver.find_element_by_xpath("//span[text()='J.K. Rowling']/../..//a")
link_autora.click()

# Extrai as informações da página da autora
nome_autora = Chrome.find_element_by_xpath("//h3[text()='J.K. Rowling']/following-sibling::span").text
data_nascimento = driver.find_element_by_xpath("//span[text()='Born']/following-sibling::text()").strip()
local_nascimento = driver.find_element_by_xpath("//span[text()='Birthplace']/following-sibling::text()").strip()
descricao = driver.find_element_by_xpath("//div[@class='author-description']").text

# Extrai as citações da autora e suas tags
citacoes = []
tags = []
while True:
    for citacao in driver.find_elements_by_xpath("//span[text()='J.K. Rowling']/../preceding-sibling::span"):
        citacoes.append(citacao.text)
        for tag in citacao.find_elements_by_xpath("../a"):
            tags.append(tag.text)
    try:
        # Tenta clicar no botão "Next" para ir para a próxima página
        botao_next = driver.find_element_by_xpath("//li[@class='next']/a")
        botao_next.click()
    except:
        # Sai do loop caso não exista mais botão "Next"
        break

# Imprime as informações e as citações e tags da autora
print("Nome da autora:", nome_autora)
print("Data de nascimento:", data_nascimento)
print("Local de nascimento:", local_nascimento)
print("Descrição:", descricao)
print("Citações:")
for citacao, tag in zip(citacoes, tags):
    print("- ", citacao, " (tag: ", tag, ")")

# Fecha o driver do navegador
driver.quit()
