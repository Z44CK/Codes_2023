import pandas as pd

df = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding="latin-1")
print(df.head())

print(df.Região.value_counts())

quantidade_reclamacoes = df['Problema'].count()
print('Quantidade de reclamações registradas: ', quantidade_reclamacoes)

tempo_medio_resposta = df['Tempo Resposta'].mean()
tempo_maximo_resposta = df['Tempo Resposta'].max()
tempo_minimo_respoosta = df['Tempo Resposta'].min()

print("O tempo medio de reposta:", tempo_minimo_respoosta)
print("O tempo maximo de resposta:", tempo_maximo_resposta)
print("O tempo minimo de resposta:", tempo_minimo_respoosta)

nota_media_consumidor = df['Nota do Consumidor'].mean()
nota_maxima_consumidor = df['Nota do Consumidor'].max()
nota_min_consumidor = df['Nota do Consumidor'].min()

print('Nota media do Consumidor: ', nota_media_consumidor)
print('Nota maxima do Consumidor: ', nota_maxima_consumidor)
print('Nota minima do Consumidor: ', nota_min_consumidor)

correlaction = df['Nota do Consumidor'].corr(df['Tempo Resposta'])
print('Correlação entre a nota do consumidor e o tempo de reposta:', correlaction)
# A correlação pode variar de -1 a 1. Um valor próximo de 1 indica uma correlação positiva forte
# (à medida que o tempo de resposta aumenta, a nota do consumidor tende a aumentar),
# um valor próximo de -1 indica uma correlação negativa forte (à medida que o tempo de resposta aumenta,
# a nota do consumidor tende a diminuir), e um valor próximo de 0 indica uma correlação fraca ou nenhuma correlação.
#
# Interprete a correlação resultante para entender como a nota do consumidor está relacionada ao tempo de resposta.
reclamacoes_por_sexo = df['Sexo'].value_counts()
print('Quantidade de reclamações por sexo: ')
print(reclamacoes_por_sexo)

reclamacoes_por_estado = df['UF'].value_counts()
print('Quantidade de reclamações por estado: ')
print(reclamacoes_por_estado)

reclamacoes_nao_respondidas = df[df['Respondida'] == 'N']
procentagem_reclamacoes_nao_respondida = (len(reclamacoes_nao_respondidas) / len(df)) * 100
print('Porcentagem de reclamações não respondidas: ', reclamacoes_nao_respondidas, '%')
