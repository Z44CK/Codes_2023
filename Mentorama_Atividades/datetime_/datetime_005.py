# Escreva scripts para mostrar os diversos formatos de data e tempo conforme abaixo:
# Data e hora atual
# Ano atual
# Mês atual
# Numero da semana do ano
# Dia atual da semana
# Dia do ano
# Dia do mês
# Dia da semana

import time
import datetime


def data_hora_atal():
    datetime.datetime.now()
    print(time.strftime('Data e Hora tual: %d/%m/%y - %H:%M:%S', time.localtime()))


data_hora_atal()
print()


def ano_atual():
    data_ano = datetime.date.today()
    atual_ano = data_ano.year
    print('Ano Atual:', atual_ano)


ano_atual()
print()


def mes_atual():
    mes_ano = datetime.date.today()
    mes_agora = mes_ano.month
    print('Mes Atual:', mes_agora)


mes_atual()
print()


def semana_ano():
    numero_semana = datetime.datetime.now()
    semana_dia = numero_semana.isocalendar()[1]
    print('Numero da semana do ano:', semana_dia)


semana_ano()
print()


def dia_atual_semana():
    atual_dia_semana = datetime.date.today().strftime('%A')
    dia_da_semanas = atual_dia_semana
    print('Dia atual da semana: ', dia_da_semanas)


dia_atual_semana()
print()


def dia_ano():
    data_atual = datetime.datetime.now()
    dia_do_ano = (data_atual - datetime.datetime(data_atual.year, 1, 1)).days + 1
    print('Dia do ano:', dia_do_ano)


dia_ano()
print()


def dia_mes():
    dia_mes_atual = datetime.datetime.now().day
    print("Dia do mês:", dia_mes_atual)


dia_mes()
print()


def dia_da_semana():
    dias_semana_numero = datetime.datetime.now().weekday()
    dias_semana = ['Segunda-feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo']
    dia_semana = dias_semana[dias_semana_numero]
    print('Dia da semana:', dia_semana)


dia_da_semana()
