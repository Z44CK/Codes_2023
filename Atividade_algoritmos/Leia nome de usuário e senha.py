# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input('Informe o nome de usuario: ')
password = input('Informe a senha: ')
while nome == password:
    print('ERROR!, A senha não pode ser igual ao nome de usuario')
    nome = input('Digite o usuario novamente: ')
    password = input('Digite a senha novamente: ')
else:
    print('Cadastro efetuado com sucesso!')
    
