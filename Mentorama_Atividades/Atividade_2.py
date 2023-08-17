# ----------------------------------> Questao 1

lista_pessoas = []

while True:
    pessoa = {}

    nome = input('Informe o nome:  (ou "sair para encerrar"): ')
    if nome.lower() == 'sair':
        break

    sexo = input('Informe o sexo: ')
    idade = int(input('Informe a idade:'))

    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade

    lista_pessoas.append(pessoa)

    print(lista_pessoas)
    for pessoa in lista_pessoas:
        print('Nome:', pessoa['nome'])
        print('Sexo:', pessoa['sexo'])
        print('Idade:', pessoa['idade'])
        print()


quantidade_pessoas = len(lista_pessoas)
print('Quantidade de pessoas cadastradas: ', quantidade_pessoas)


soma_idades = 0
for pessoa in lista_pessoas:
    soma_idades += pessoa['idade']

media_idade = soma_idades / quantidade_pessoas
print('A media da idade das pessoas cadastradas e: ', media_idade)

lista_mulheres = []
for mulher in lista_pessoas:
    if mulher['sexo'].lower() == 'feminino':
        lista_mulheres.append(mulher)

print('Lista de Mulheres: ')
for mulher in lista_mulheres:
    print('Nome: ', mulher['nome'])
    print('Sexo: ', mulher['sexo'])
    print('Idade: ', mulher['idade'])
    print()

idade_acima_media = []

for pessoa in lista_pessoas:
    if pessoa['idade'] > media_idade:
        idade_acima_media.append(pessoa)

print('Pessoas com idade acima da media: ')
for pessoa in idade_acima_media:
    print('Nome: ', pessoa['nome'])
    print('Sexo: ', pessoa['sexo'])
    print('Idade: ', pessoa['idade'])
    print()

# ---------------------------------------------------------------------- Resolução do problema com list comprehension abaixo

lista_pessoas = []

while True:
    pessoa = {}

    nome = input('Informe o nome (ou digite "sair" para encerrar: ')
    if nome.lower() == "sair":
        print('Programa encerrado!')
        break
    sexo = input('Informe o sexo: ')
    idade = int(input('informe a idade: '))

    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade

    lista_pessoas.append(pessoa)

    print(lista_pessoas)
    print('Nome: ', pessoa['nome'])
    print('Sexo: ', pessoa['sexo'])
    print('Idade:', pessoa['idade'])
    print()

quantidade_pessoas = len(lista_pessoas)
print('A Quantidade de pessoas cadastradas sao: ', quantidade_pessoas)

soma_idade = sum([pessoa['idade'] for pessoa in lista_pessoas])
media_idade = soma_idade / quantidade_pessoas
print('A media das idades sao: ', media_idade)


lista_mulher = [mulher for mulher in lista_pessoas if mulher['sexo'].lower() == 'feminino']
for mulher in lista_mulher:
    print('Nome:', mulher['nome'])
    print('Sexo: ', mulher['sexo'])
    print('Idade: ', mulher['idade'])
    print()

idade_acima_media = [pessoa for pessoa in lista_pessoas if pessoa['idade'] > media_idade]
for pessoa in idade_acima_media:
    print('Nome: ', pessoa['nome'])
    print('Sexo: ', pessoa['sexo'])
    print('Idade: ', pessoa['idade'])

print(lista_mulher)
