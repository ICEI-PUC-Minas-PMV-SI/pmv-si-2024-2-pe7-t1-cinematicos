# Conhecendo os dados
A partir daqui, exploramos a base de dados do dataset utilizado, para compreender sua estrutura, detectar outliers e avaliar as relações entre as variáveis analisadas. As análises incluem medidas de tendência central, dispersão e visualizações gráficas.

## Carregamento e Visualização Inicial dos Dados
O dataset contém informações sobre filmes e séries, incluindo título, ano de lançamento, classificação indicativa, duração, gênero, avaliação, descrição, elenco e número de votos. As primeiras linhas do dataset foram visualizadas para entender a estrutura dos dados.
## Medidas de Tendência Central e Dispersão
As colunas numéricas rating e votes foram analisadas para calcular medidas de tendência central e dispersão.
A tabela a seguir resume as medidas calculadas:
>>>>img.metrics1
## Visualização Gráfica
Para visualizar a distribuição dos dados, foram criados histogramas e box plots para as variáveis rating e votes.
>>>img.rating_votes

Análise Gráfica:
1. Distribuição de Ratings:
- A maioria dos filmes tem avaliações entre 5 e 9.
- A distribuição é levemente assimétrica à esquerda, com concentração maior em torno de 7.
2. Distribuição de Votos:
- A maioria dos filmes tem menos de 10.000 votos.
- A escala logarítmica mostra que há alguns filmes com um número muito alto de votos (cauda longa).

Medidas de Correlação
  Para entender a relação entre as variáveis, foi criada uma matriz de correlação entre rating e votes.

Análise de Correlação:
- A correlação entre rating e votes é de aproximadamente 0.24, indicando uma correlação positiva fraca. Ou seja, filmes com mais votos tendem a ter uma avaliação ligeiramente mais alta, mas a relação não é forte.
- O gráfico de dispersão mostra uma dispersão ampla, com filmes populares (muitos votos) não necessariamente recebendo avaliações muito altas.

## Descrição dos achados
A análise descritiva e exploratória revelou vários insights importantes:
### Centralidade dos Dados:
- A maioria dos filmes e séries tem avaliações entre 6 e 8.
- A mediana de votos é 1.187, mostrando que metade dos filmes tem menos de 1.187 votos.
### Variabilidade dos Dados:
- A dispersão dos votos é muito alta, com um desvio padrão grande. Isto indica a presença de filmes com muitos votos que podem influenciar a análise.
- O desvio padrão do rating é mais contido, sugerindo uma distribuição mais consistente das avaliações.
### Correlação entre os Atributos:
- A correlação entre rating e votes é fraca (0.24), indicando que o número de votos influencia pouco a avaliação geral do filme.
- Os outliers identificados no número de votos (filmes com muitos votos) destacam a variabilidade no sucesso popular dos filmes.

## Ferramentas
A maior parte das análises foi realizada utilizando a linguagem de programação Python, com as bibliotecas:

Pandas: Para manipulação e análise de dados.
Seaborn e Matplotlib: Para visualização dos dados e criação de gráficos.
Jupyter Notebook: Para desenvolvimento iterativo de códigos e visualização das análises.

>>>>> modelo para apagar depois <<<<<<<
# Conhecendo os dados

Nesta seção, deverá ser registrada uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas.

Para isso, sugere-se que sejam utilizados cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; sejam exploradas medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; sejam utilizados gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; sejam analisadas as relações entre as variáveis por meio de análise de correlação, gráficos de dispersões, mapas de calor, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar.  Além disso, inclua e comente os trechos de código mais relevantes desenvolvidos para realizar suas análises. Na pasta "src", inclua o código fonte completo.

## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a atenção? Foi possível identificar correlação entre os atributos? Que tipo de correlação (forte, fraca, moderada)? 

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.
