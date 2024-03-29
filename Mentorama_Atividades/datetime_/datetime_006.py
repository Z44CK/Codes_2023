# Escreva um programa python capaz de conveter uma string em data e hora.
# string de exemplo: 01 janeiro de 2021 13h53, resultado esperado 2021-01-01 13:53:00

from datetime import datetime


def converter_string_para_data_hora(string_data):
    meses = {
        'janeiro': 1
    }

    partes = string_data.split()
    dia = int(partes[0])
    mes = meses[partes[1]]
    ano = int(partes[3])
    hora, minutos = map(int, partes[4].replace('h', ':').split(':'))

    data_hora = datetime(ano, mes, dia, hora, minutos)
    return data_hora


string_exemplo = "01 janeiro de 2021 13h53"
data_hora_convertida = converter_string_para_data_hora(string_exemplo)
print("Resultado:", data_hora_convertida)
