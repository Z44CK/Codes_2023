# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Informe o nome:'))
while len(nome) <= 3:
    print('ERROR!, o nome deve ter mais que três caracteres')
    nome = str(input('Informe o nome: '))

idade = int(input('Informe a idade: '))
while (idade > 150) or (idade < 0):
    print('ERROR!, a idade deve ser entre 0 a 150 anos')
    idade = int(input('Informe a idade: '))

salario = float(input('Informe o salario: '))
while salario < 0:
    print('ERROR!, O slario deve ser maior que zero')
    salario = float(input('Informe o salario: '))

sexo = input('Informe o sexo (f ou m): ')
while sexo.lower() != 'f' and sexo.lower() != 'm':
    print('Sexo inválido')
    sexo = input('Informe o sexo (f ou m): ')
    

estado_civil = str(input('Informe o estado civil(s, c, v, d): ')).lower()
while (estado_civil != 's'
       and estado_civil != 'c'
       and estado_civil != 'v'
       and estado_civil != 'd'):
    print('ERROR!, Estado civil invalido!')
    estado_civil = str(input('Informe o estado civil(s, c, v, d): '))
