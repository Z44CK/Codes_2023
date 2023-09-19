import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import reciprocal

# Carregar o conjunto de dados MNIST
mnist = fetch_openml("mnist_784", version=1)
X, y = mnist.data, mnist.target.astype(int)

# Dividir o conjunto de dados em treinamento (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definir a grade de hiperparâmetros para pesquisa aleatória
param_dist = {
    'C': reciprocal(0.001, 10),
    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
    'gamma': reciprocal(0.001, 0.1),
}

# Criar um classificador SVM
clf = SVC()

# Realizar a pesquisa aleatória com validação cruzada (k = 5)
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=10, cv=5, n_jobs=-1)
random_search.fit(X_train, y_train)

# Obter os melhores hiperparâmetros
best_params = random_search.best_params_

# Imprimir os melhores hiperparâmetros
print("Melhores Hiperparâmetros Encontrados:")
print(best_params)

# Treinar o modelo com os melhores hiperparâmetros no conjunto de treinamento completo
best_model = SVC(**best_params)
best_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste usando validação cruzada (k = 5)
y_pred = cross_val_predict(best_model, X_test, y_test, cv=5, n_jobs=-1)

# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia no conjunto de teste: {accuracy:.4f}')

# Exibir o relatório de classificação
report = classification_report(y_test, y_pred)
print("Relatório de Classificação:\n", report)

# Criar a matriz de confusão
confusion = confusion_matrix(y_test, y_pred)

# Exibir a matriz de confusão usando o seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsto')
plt.ylabel('Verdadeiro')
plt.title('Matriz de Confusão')
plt.show()
