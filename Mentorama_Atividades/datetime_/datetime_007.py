# Programa para subtrair 8 dias da data atual:
# data atual 25/01/2021, data esperada 17/01/2021

import datetime

data_inicial = '25/01/2021'
converter_1 = datetime.datetime.strptime(data_inicial, '%d/%m/%Y')
resultado_sub = converter_1 - datetime.timedelta(days=8)
print('Data original:', converter_1.strftime('%d/%m/%Y'))
print('Resultado final:', resultado_sub.strftime('%d/%m/%Y'))
  
