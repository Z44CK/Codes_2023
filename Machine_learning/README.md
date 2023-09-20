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
3 - Faça uma pesquisa para conhecer um pouco mais sobre o universo de Machine Learning e responda a seguir:
a- Qual é a diferença entre um parametro de modelo e um algoritmo de aprendizagem de hiperparametro?
Um parametro de modelo é uma variavel do modelo selecionada que pode ser estimada ajustando os dados fornecidos ao modelo
-------------------------------------------------------------------------------------------
Um hiperparâmetro de modelo é o parâmetro cujo valor é definido antes de o modelo iniciar o treinamento.
Eles não podem ser aprendidos ajustando o modelo aos dados.
------------------------------------------------------------------------------------------
b - Você pode citar quatro dos principais desafios do aprendizado de maquina?
1 Pessimas intenções, pois caso ensinarmos um exercito de maquinas a matar pessoas, isso seria muito ruim.
2 Parâmetros de sistema nem sempre incluem ética.
3 Relatividade ética.
4 Correlações falsas
--------------------------------------------------------------------------------------------
c - Se o seu modelo tem um ótimo desempenho nos dados de treinamento, mas generaliza mal para novas instancais, o que esta acontecendo?
Você pode citar três soluções?
 Três soluções para lidar com o overfitting: regularizar o modelo, aumentar os dados  e simplificar o modelo
 e alem dessas soluções sempre é importante monitorar o desempenho.
--------------------------------------------------------------------------------------------

d - O que é um conjunto de teste e por que você deve usa-lo?
Um conjunto de teste, é uma parte essencial de qualquer processo de treinamento e avaliação de modelos de aprendizado de máquina e inteligência artificial. 
Devemos usa-los para evitar overfitting, ajuste de hiperparametros, etc...
---------------------------------------------------------------------------------------------
e - Qual é o proposito de um conjunto de validação?
O conjunto de validação tem vários propósitos importantes no contexto do treinamento de modelos de aprendizado de máquina e inteligência artificial,
É uma parte essencial do processo de desenvolvimento de modelos.
---------------------------------------------------------------------------------------------
f - O que pode dar errado se você ajustar o hiperparametro usando o conjunto de teste?
Ajustar hiperparâmetros usando o conjunto de teste é uma prática que deve ser evitada,
e há várias razões importantes para isso. 
Quando você ajusta os hiperparâmetros com base no conjunto de teste, pode enfrentar os seguintes problemas,
overfitting do conjunto de teste, superestimação do desempenho, generalização pobre dentre outros
