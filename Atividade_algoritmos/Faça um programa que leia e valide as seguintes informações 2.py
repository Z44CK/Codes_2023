# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
while True:
    s = str(input('Opções: (1-Iniciar) (2-Encerrar programa): '))
    if s == '1':
        nome = str(input('Informe o nome: '))
        while len(nome) < 3:
            print('Nome invalido, digite novamente')
            nome = str(input('Informe o nome: '))
        if len(nome) > 3:
            print(f'Nome:{nome}')

        idade = int(input('Informe a idade:'))
        while (idade > 150) and (idade < 0):
            print('ERROR!, Insira um valor valido, (0 a 150)!')
            idade = int(input('Informe a idade: '))
        if 150 <= idade >= 0:
            print(f'Idade:{idade}')

        salario = float(input('Informe o salario maior que 0: '))
        if salario < 0:
            print('Valor incorreto!')
        elif salario > 0:
            print(f'Salario:{salario:.2f}')

        sexo = str(input('Informe o sexo (f)-feminino / (m)-masculino / (p)-prefiro não informar: '))
        if sexo == 'f':
            print('Sexo feminino')
        elif sexo == 'm':
            print('Sexo masculino')
        elif sexo == 'p':
            print('Prefiro não informar!')
        else:
            print('Valor incorreto, insira as informações pedidas acima!')

        est_civil = str(input('Informe o estado civil: (s)-solteiro / (c)-casado / (v)-viuvo / (d)-divorciado:'))
        if est_civil == 's':
            print('Solteiro')
        elif est_civil == 'c':
            print('Casado')
        elif est_civil == 'v':
            print('Viuvo')
        elif est_civil == 'd':
            print('Divorciado')
        else:
            print('Valor incorreto, insira as informações pedidas acima!')

    elif s == '2':
        print('Programa encerrado com exito!')
        break
