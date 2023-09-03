import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding="latin-1")

segmento_mercado_counts = df['Segmento de Mercado'].value_counts()
segmento_mercado_labels = segmento_mercado_counts.index

plt.figure(figsize=(20, 8))
sns.barplot(x=segmento_mercado_labels, y=segmento_mercado_counts, palette='pastel')

for index, value in enumerate(segmento_mercado_counts):
    plt.text(index, value + 10, str(value), ha='center', fontsize=9)

plt.title('Distribuição de Reclamações por Segmento de Mercado', fontsize=14)
plt.xlabel('Segmento de Mercado', fontsize=12)
plt.ylabel('Contagem', fontsize=12)
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
