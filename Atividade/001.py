# Desenvolva um web scraper para obter um arquivo YAML:
# realize a raspagem dos dados da página
# www.w3schools.io/file/yaml-sample-example/
# Extraia o exemplo de arquivo YAML da pagina
# utilize REGEX para extrair os comentarios contidos no exemplo e imprima na tela
# Escreva um arquivo YAML os exemplos extraidos do arquivo YAML
import re
import requests
import yaml

# URL da página que você deseja raspar
url = "https://www.w3schools.io/file/yaml-sample-example/"

# Realizando a solicitação para obter o conteúdo da página
response = requests.get(url)
content = response.text

# Usando regex para encontrar o exemplo de arquivo YAML na página
yaml_example_pattern = r'```yaml(.*?)```'
yaml_example_matches = re.findall(yaml_example_pattern, content, re.DOTALL)

if yaml_example_matches:
    yaml_example = yaml_example_matches[0].strip()  # Obtendo o exemplo de YAML

    # Usando regex para extrair comentários do exemplo YAML
    comments_pattern = r'#(.*?)\n'
    comments = re.findall(comments_pattern, yaml_example)

    # Imprimindo os comentários na tela
    print("Comentários encontrados no exemplo de YAML:")
    for comment in comments:
        print(comment.strip())

    # Escreve os exemplos extraídos em um arquivo YAML
    with open("exemplo_yaml.yaml", "w") as file:
        yaml.dump(yaml.safe_load(yaml_example), file, default_flow_style=False)
else:
    print("Exemplo de arquivo YAML não encontrado na página.")
