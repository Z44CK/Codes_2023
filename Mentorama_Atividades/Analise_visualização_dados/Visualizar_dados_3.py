import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding="latin-1")

# Frequencia de reclamaçoes respondidas e não respondidas
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Respondida', palette='Set3',)
plt.title('Frequencia de Reclamações respondidas e não respondidas')
plt.xlabel('Respondiuda')
plt.ylabel('Frequencia')
plt.xticks([0, 1], ['Não Respondida', 'Respondida'])
plt.show()
