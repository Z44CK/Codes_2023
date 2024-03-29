# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


while True:
    nome = input('Informe o nome: ')
    if len(nome) <= 3:
        print('O nome deve possuir mais que três caracteres!')
        continue

    idade = int(input('Informe a idade: '))
    if 0 >= idade <= 150:
        print(f'A idade deve estar entre 0 a 150 anos!')
        continue

    salario = float(input('Informe o salario: '))
    if salario <= 0:
        print(f'O salario deve ser maior que zero')
        continue

    sexo = input('Informe o sexo: (f-feminino, m-masculino): ')
    if sexo not in ['f', 'm']:
        print('Informe um sexo válido: f - feminino, m - masculino!')
        continue

    estado_civil = input('Estado civil: (s-solteiro, c-casado, v-viuvo, d-divorciado): ')
    if estado_civil not in ['s', 'c', 'v', 'd']:
        print('Informe um estado civil valido: s - solteiro, c - casado, v - viuvo, d - divorciado!')
        continue

    break

print(f'Nome:{nome} ')
print(f'Idade: {idade} anos ')
print(f'Salario: R${salario:.2f}')
print(f'Sexo: {"Feminino" if sexo == "f" else "Masculino"}')
print(f'Estado Civil: {"Solteiro" if estado_civil == "s" else "Casado"if estado_civil == "c" else "Viuvo" if estado_civil == "v" else "Divorciado"}')
