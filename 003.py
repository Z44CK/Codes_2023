# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Data:dd/mm/aaaa: ')

dia, mes, ano = map(int, data.split('/'))
bissexto = (ano % 400 == 0) or (ano % 4 == 0) or (ano % 100 != 0)

if (0 < dia <= 31 and
        0 < mes <= 12 and
        1900 <= ano <= 2099 and
        (mes != 2 or (mes == 2 and (0 < dia <= 28 or (dia == 29 and bissexto))))):
    print('Data Válida!')
else:
    print('Data Inválida!')
