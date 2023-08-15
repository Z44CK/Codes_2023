# Crie um programa para exibir um lista entre duas datas, considerando o passo de um dia e reproduza o intervalo
# entre as datas 16/10/87 e 25/10/87 

from datetime import datetime, timedelta


def intervalo_data(data_inicial, data_final):
    lista_datas = []
    data_atual = data_inicial

    while data_atual <= data_final:
        lista_datas.append(data_atual.strftime('%d/%m/%y'))
        data_atual += timedelta(days=1)

    return lista_datas


data_inicial_str = '16/10/87'
data_final_str = '25/10/87'

data_inicial = datetime.strptime(data_inicial_str, '%d/%m/%y')
data_final = datetime.strptime(data_final_str, '%d/%m/%y')

if data_inicial <= data_final:
    lista_entre_datas = intervalo_data(data_inicial, data_final)
    print('Lista de datas entre as datas fornecidas:')
    for data in lista_entre_datas:
        print(data)
else:
    print('A data inicial dever ser anterior ou igual a data final.')
