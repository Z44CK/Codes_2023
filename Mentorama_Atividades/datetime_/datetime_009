// Faça um programa para calcular a diferença de dias entre antes de ontem
// e depois de amanhã.

from datetime import datetime, timedelta

hoje = datetime.now()
anteontem = hoje - timedelta(days=2)
depois_de_amanha = hoje + timedelta(days=2)

diferenca_em_dias = (depois_de_amanha - anteontem).days

print(f"A diferença em dias entre anteontem ({anteontem.date()}) e depois de amanhã ({depois_de_amanha.date()})"
      f" é de {diferenca_em_dias} dias.")
  
