# Escrever scripts que demonstre os diversos formatos de tempo conforme segue:
# A - Impressão da época padrão
# B - Segundos que se passaram desde a época padrão
# C - Imprime dados de tempo no momento atual
# D - Cria um objeto time.localtime() e imprime os valores da hora, minutos e segundos 
# E - Imprime se no momento atual estamos no horario de verão ou não

import time
import datetime


def dataehorapadrao():
    epoca_padrao = datetime.datetime(1970, 1, 1)
    formato_data_hora = '%Y/%m/%d - %H:%M:%S'
    epoca_padrao_formatada = epoca_padrao.strftime(formato_data_hora)
    print(f'Epoca padrão: {epoca_padrao_formatada}')


dataehorapadrao()


def segundos_epoca():
    data_hora_atual = datetime.datetime.now()
    epoca_padrao = datetime.datetime(1970, 1, 1)
    diferenca = data_hora_atual - epoca_padrao
    print(f'Segundos passados desde a epoca padrão é:{diferenca:} segundos')


segundos_epoca()


def momentoatual():
    datetime.datetime.now()
    print(time.strftime('Tempo no momento atual %d/%m/%Y - %H:%M:%S:', time.localtime()))


momentoatual()


def hora_minutos_segundos():
    hora_local_atual = time.localtime()

    horas = hora_local_atual.tm_hour
    minutos = hora_local_atual.tm_min
    segundos = hora_local_atual.tm_sec

    print(f'Horas: {horas:.2f}')
    print(f'Minutos: {minutos:.2f}')
    print(f'Segundos: {segundos:.2f}')


hora_minutos_segundos()


def horario_verao():
    data_hora_hoje = time.localtime()
    esta_no_horario_verao = data_hora_hoje.tm_isdst

    if esta_no_horario_verao:
        print('Está no horario de verão.')
    else:
        print('Não está no horario de verão.')


horario_verao()
