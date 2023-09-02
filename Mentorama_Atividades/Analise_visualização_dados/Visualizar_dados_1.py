# Grafico que mostra a sequencia de reclamações por sexo

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding="latin-1")

# Frequencia de reclamações por sexo:
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")
sns.countplot(data=df, x='Sexo', palette='Set1')

plt.title('Frequencia de Reclamações por Sexo')
plt.xlabel('Sexo', fontsize=14)
plt.ylabel('Frequencia', fontsize=14)


plt.show()
