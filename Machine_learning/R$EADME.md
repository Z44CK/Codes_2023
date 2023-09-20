2 - Apos a etapa de treinamento, analise o modelo e responda as questões a seguir:
a - Qual a acuracia do modelo? justifique
Acurácia no conjunto de teste: 8.92%, O pré-processamento de dados, 
incluindo a normalização e o redimensionamento das imagens podem afetar 
significativamente o desempenho do modelo.
--------------------------------------------------------------------------------------------
b - O modelo teve uma boa performace? Justifique
Não, o modelo não teve uma boa performace, Uma acurácia tão baixa pode sugerir que o modelo sofre de overfitting,
ou seja, ele se ajustou demais aos dados de treinamento e não generaliza bem para novos dados.
-------------------------------------------------------------------------------------------
c - Quais foram os melhores parametros escolhidos? justifique
os melhores parametros foi escolhido por meio de uma busca aleatória
(Random Search) usando a classe RandomizedSearchCV, Os melhores parâmetros podem variar
dependendo da execução da busca aleatória.
------------------------------------------------------------------------------------------
d - Quais as principais dificuldades encontradas para a criação do seu modelo de classificação?
Para mim a maior dificuldade que encontrei foi conseguir implementar a grade de hiperparametros
para uma busca aleatoria e inicializar a busca aleatoria com validação cruzada.
-----------------------------------------------------------------------------------------
3 - 
