import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding="latin-1")

# Frequencia por estado
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='UF', palette='Set2', order=df['UF'].value_counts().index)

plt.title('Frequencia de reclamações por estado')
plt.xlabel('Estado')
plt.ylabel('Frequencia')

plt.show()
