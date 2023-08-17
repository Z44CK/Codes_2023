# Calcula o numero de dias entre dois datetimes
# a diferença entre os dias deve ser de 10 dias.

from datetime import datetime, timedelta

d1 = datetime(2023, 8, 15)
d2 = datetime(2023, 8, 5)

diferenca_esperada = timedelta(days=10)
diferenca_real = d1 - d2
if diferenca_real == diferenca_esperada:
    print(f'A diferença entre as datas {d1} e {d2} é de:', diferenca_real)
else:
    print('A diferença entre as datas não é de 10 dias!')
  
