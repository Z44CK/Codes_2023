# Quiz - Programa que gera 5 perguntas de sim ou não, caso as respostas sejam positivas mais de uma vez o programa executa uma condição abaixo.
# caso não, o programa printa inocente na tela e finaliza.


resposta = 0

resposta += int(input('a-Telefonou para a vitima? (1-Sim/0-Não): '))
resposta += int(input('b-Esteve no local do crime? (1-Sim/0-Não): '))
resposta += int(input('c-Mora perto da vitima? (1-Sim/0-Não): '))
resposta += int(input('d-Devia para a vitima? (1-Sim/0-Não): '))
resposta += int(input('e-Já trabalhou com a vitima? (1-Sim/0-Não): '))

if resposta == 2:
    print('Suspeita!')
elif 3 <= resposta <= 4:
    print('Cúmplice!')
elif resposta == 5:
    print('Assassino!')
else:
    print('Inocente!')
