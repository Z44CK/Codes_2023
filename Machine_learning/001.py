from keras.datasets import mnist
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neural_network import MLPClassifier
from scipy.stats import uniform, randint
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# carregando o dados do mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Redimensionando as imagens para um vetor unidimensional
x_train = x_train.reshape(x_train.shape[0], -1)

# Normalizando os valores de pixel para estar no intervalo [0, 1]
x_train = x_train.astype('float32') / 255

# Definindo o modelo MLP
model = MLPClassifier()

# Definindo a grade de hiperparâmetros para a busca aleatória
param_dist = {
    'hidden_layer_sizes': [(64,), (128,), (64, 64), (128, 64)],
    'alpha': uniform(0.0001, 0.1),
    'activation': ['logistic', 'tanh', 'relu'],
    'learning_rate': ['constant', 'invscaling', 'adaptive'],
    'learning_rate_init': uniform(0.001, 0.1),
    'max_iter': randint(100, 1000),
}
# Inicializando a busca aleatória com validação cruzada
random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=5, random_state=42, n_jobs=-1,
                                   verbose=2)

# Realizando a busca aleatória
random_search.fit(x_train, y_train)

# Melhores parâmetros encontrados pela busca aleatória
best_params = random_search.best_params_
print("Melhores Parâmetros Encontrados:", best_params)

# Treinando o modelo com os melhores parâmetros
best_model = MLPClassifier(**best_params)
best_model.fit(x_train, y_train)

# Avaliando o modelo no conjunto de teste
x_test = x_test.reshape(x_test.shape[0], -1)
x_test = x_test.astype('float32') / 255
accuracy = best_model.score(x_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

# numeros de folds(k)
k = 5
# inicializa o objeto k-fold
kf = KFold(n_splits=k, shuffle=True, random_state=42)

# dividindo o conjunto de treinamentos em k folds
for fold, (train_indices, val_indices) in enumerate(kf.split(x_train)):
    x_train_fold, x_val_fold = x_train[train_indices], x_train[val_indices]
    y_train_fold, y_val_fold = y_train[train_indices], y_train[val_indices]

    print(f'Dobra {fold + 1} - Tamanho do conjunto de treinamento: {len(x_train_fold)} amostras')
    print(f'Dobra {fold + 1} - Tamanho do conjunto de validação: {len(x_val_fold)} amostras')


# divindo o treinamento e teste em 80/20
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

print(f"Tamanho do conjunto de treinamento: {len(x_train)} amostras")
print(f"Tamanho do conjunto de validação: {len(x_val)} amostras")
print(f"Tamanho do conjunto de teste: {len(x_test)} amostras")

y_pred = best_model.predict(x_test)
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', camp='Blues', cbar=False)
plt.xlabel('Previsão')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusão')
plt.show()
