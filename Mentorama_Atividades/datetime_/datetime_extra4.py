import datetime
hora_hoje = datetime.datetime.now().time()
novo_horario = hora_hoje.hour - 3
data_fuso = datetime.time(hour=hora_hoje.hour - 3, minute=hora_hoje.minute, second=hora_hoje.second)
print(data_fuso)
