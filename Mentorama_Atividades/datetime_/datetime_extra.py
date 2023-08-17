from datetime import datetime


def convert_datetime_string(string_data):
    dia_n = {
        'Quarta,': 0


    }
    partes = string_data.split()
    dia = dia_n[0]
    mes = int(1)
    ano = int(2)

    data_hora = datetime(dia, mes, ano)
    return data_hora


string_texto = 'Quarta, 16 de outubro de 2023'
data_hora_convertida = convert_datetime_string(string_texto)
print(data_hora_convertida)
