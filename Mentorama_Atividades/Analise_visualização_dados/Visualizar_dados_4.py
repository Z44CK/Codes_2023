// -- Projeto de Satisfação do cliente
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding="latin-1")
plt.figure(figsize=(9, 5))
sns.histplot(data=df, x='Faixa Etária', hue='Nota do Consumidor', palette='coolwarm', multiple='stack')
plt.title('Satisfação do Consumidor por faixa etaria')
plt.xlabel('Faixa Etaria', fontsize=13)
plt.ylabel('Contagem', fontsize=13)
plt.xticks(rotation=45)
plt.show()
