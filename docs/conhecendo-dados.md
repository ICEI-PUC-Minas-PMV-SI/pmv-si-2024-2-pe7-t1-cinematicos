# Conhecendo os dados
A partir daqui, exploramos a base de dados do dataset utilizado, para compreender sua estrutura, detectar outliers e avaliar as relações entre as variáveis analisadas. As análises incluem medidas de tendência central, correlação, dispersão, entre outras visualizações gráficas.

O dataset possuí 24 colunas das quais estão dividas entre 6 colunas Quantitativas e 18 colunas Qualitativas.

Colunas Quantitativas:

- Budget: Orçamento.
- Popularity: Medida de popularidade.
- Revenue: Receita gerada.
- Vote_average: Média de votos ou avaliações.
- Vote_count: Número total de votos recebidos.
- Runtime: Duração do filme em minutos.
  
Colunas Qualitativas:

- Index: Índice (numérica, mas categórica no contexto do dataset).
- Genres: Uma string conmtendo múltiplos gêneros.
- Homepage: URL dos sites principais.
- id: Identificador único (qualitativa, numérico no formato).
- Keywords: Palavras-chave descrevendo temas ou elementos importantes .
- Original_language: Idioma original que o filme foi produzido.
- Original_title: Título original.
- Overview: Resumo ou sinopse.
- Production_companies: Companhias envolvidas na produção do filme.
- Production_countries: Lista de países onde o filme foi produzido.
- Release_date: Data de lançamento (qualitativa, tratada como texto).
- Spoken_languages: Idiomas falados.
- Status: Status de lançamento:
- Tagline: Frase de efeito ou slogan do filme.
- Title: Título atual.
- Cast: Lista de atores principais.
- Crew: Lista da equipe técnica e criativa envolvida no filme.
- Director: Diretor.

### Estatísticas Descritivas ###

A estátistica descritiva fornece uma visão geral dos dados numéricos, resumindo suas principais características:

| Estatística       | vote_average | vote_count  | budget          | popularity    | revenue         |
|-------------------|--------------|-------------|------------------|---------------|------------------|
| count             | 4803.000000  | 4803.000000 | 4.803000e+03     | 4803.000000   | 4.803000e+03     |
| mean              | 6.092172     | 690.217989  | 2.904504e+07     | 21.492301     | 8.226064e+07     |
| std               | 1.194612     | 1234.585891 | 4.072239e+07     | 31.816650     | 1.628571e+08     |
| min               | 0.000000     | 0.000000    | 0.000000e+00     | 0.000000      | 0.000000e+00     |
| 25%               | 5.600000     | 54.000000   | 7.900000e+05     | 4.668070      | 0.000000e+00     |
| 50% (mediana)     | 6.200000     | 235.000000  | 1.500000e+07     | 12.921594     | 1.917000e+07     |
| 75%               | 6.800000     | 737.000000  | 4.000000e+07     | 28.313505     | 9.291719e+07     |
| max               | 10.000000    | 13752.000000| 3.800000e+08     | 875.581305    | 2.787965e+09     |


Contagem (count): Para todas as métricas possuindo 4803 registros.

Média (mean): 
- A média do vote_average é de aproximadamente 6.09, indicando que em média os filmes avaliados têm uma nota razoável.
- O vote_count médio é 690.21, o que mostra que, em média, cada filme recebeu um número moderado de votos. No entanto, os dados dos quartis demonstram que poucos filmes concentram grande quantidade de votos. 
- O budget médio seria de aproximadamente 29 milhões e a revenue média seria cerca de 82 milhões, indicando que a média dos filmes geram uma receita significativamente maior que média da receita usada em seu orçamento.
- A média de popularity é 21.49, mostrando uma grande variação entre os filmes.

Desvio Padrão (std): 
- O desvio padrão do vote_average (1.19) indica que as avaliações dos filmes variam moderadamente em relação à média.
- O vote_count tem um desvio padrão de 1234.59, sugerindo que alguns filmes recebem muitos votos acima da média.
- O budget e a revenue têm desvios de padrão altos, o que indica que pode haver uma grande variação nos valores; alguns filmes têm orçamentos muito altos e outros são significativamente mais baixos.

Mínimo e Máximo: 
- O vote_average varia de 0.00 a 10.00, indicando que existem filmes que podem ter sido muito mal avaliados ou sem avaliação e outros que são considerados excelentes, considerando uma média que 50% dos filmes possui uma nota aceitável de 6.09.
- O vote_count varia de 0 a 13752, o que sugere que alguns filmes podem não ter recebido votos, enquanto outros tiveram uma recepção extremamente alta aos votos.
- O budget varia de 0 a cerca de 380 milhões, mostrando uma grande variedade nos valores do orçamento de vários filmes.
- A revenue também varia bastante, de 0 a aproximadamente 2.79 bilhões, indicando que alguns filmes podem não ter conseguido nenhum lucro ou seria um dado nulo para esses filmes.

### Modas ###

- **Moda Rating**: 6.0
- **Moda Votos**: 0.0
- **Moda Orçamento**: 0
- **Moda Popularidade**: 8.902102000000003
- **Moda Receita**: 0

A moda do vote_average é 6.0, indicando que essa é a avaliação mais frequente entre os filmes.
O vote_count tem uma moda de 0.0, sugerindo que muitos filmes não receberam votos, o que pode ser um indicador de que eles não foram amplamente divulgados ou vistos. Outra hipótese é que os dados estejam incompletos.
A moda de popularidade é de 8.90, indicando que muitos filmes atingem esse nível de aceitação ou que poucos filmes se destacam significativamente.
As modas para orçamento e receita são 0, indicando que muitos filmes tiveram orçamentos baixos, não geraram receita significativa ou que os dados estão incompletos.

### Quantidade de Valores 0 por Coluna ###

Diante dos resultados descritos acima, se tornou evidente o fato do grande número de valores definidos como 0. Um levantamento foi realizado para avaliar mais a fundo o tamanho e o impacto desses casos no trabalho. 


| Coluna         | Quantidade de Valores 0 |
|----------------|-------------------------|
| index          | 1                       |
| budget         | 1037                    |
| id             | 0                       |
| popularity     | 1                       |
| revenue        | 1427                    |
| runtime        | 35                      |
| vote_average   | 63                      |
| vote_count     | 62                      |


Identificamos a presença de alguns valores iguais a 0, afetando principalmente vote_count, budget e revenue. Indicando que alguns filmes podem não ter sido suficientemente populares, ou seja, não receberam votos, não tiveram orçamento ou lucro, o que pode estar distorcendo as métricas. A presença de 1037 valores zero na coluna budget sugere que muitos filmes não têm orçamento definido, o que pode prejudicar a relação entre receita e custo de produção, levando a conclusões imprecisas sobre a viabilidade financeira. Da mesma forma, os 1427 zeros em revenue mostram que muitos filmes não geraram receita, o que pode afetar a média de receita e influenciar a análise sobre o sucesso dos filmes. Além disso, os 63 valores zero em vote_average e os 62 em vote_count revelam que alguns filmes não foram avaliados, podendo comprometer a análise de aceitação crítica e popular, podendo levar a métricas de avaliação não tão precisas. No entanto, em todos esses casos, o que parece mais crível é a incompletude dos dados. Certamente, é mais plausível pensarmos em dados de orçamento e receita não computados do que imaginar um só filme realizado sem qualquer fonte de orçamento ou receita. Além disso, estes são dados que nem sempre são amplamente divulgados por produtores e distribuidores.  


### Mapa de Calor ###

![Mapa de calor](/docs/img/mapacalor.png)

A análise do mapa de calor revelou padrões claros na correlação entre as variáveis budget, popularity, revenue, vote_average, e vote_count. Observamos uma forte correlação entre budget e revenue, sugerindo que filmes com maiores orçamentos tendem a gerar mais receita. A relação próxima entre vote_count e popularity, assim como com revenue, indica que filmes mais populares e de maior bilheteira atraem mais votos, conseguindo o engajamento de públicos maiores. No entanto, a variável vote_average parece ter uma correlação mais fraca com as outras, especialmente em relação as colunas budget e revenue. Essa fraqueza indica que a média de avaliações não é diretamente influenciada por orçamentos elevados ou receitas substanciais. Filmes com maior avaliação, muitas vezes, podem ser produções de menor escala ou de nicho que conquistaram o público por sua qualidade, enredo ou performances, desafiando a noção de que um grande orçamento é sinônimo de uma alta avaliação. Assim, o mapa de calor sugere que,enquanto os investimentos financeiros e a popularidade podem gerar receita, a qualidade percebida e o engajamento do público em relação à avaliação média podem depender de fatores mais subjetivos. Certamente esperávamos encontrar maior correlação entre o vote_average e outros parâmetros, o que pode inviabilizar uma eventual inferência do vote_average a partir de outros campos. 


### Hipótese: Diretores Renomados e Não Renomados ###

Filmes dirigidos por diretores mais renomados tendem a receber notas mais altas?

Nessa hipótese separamos os diretores entre renomados que dirigiram dois ou mais filmes e não renomados com somente 1 filme e vamos comparar a média de votos (vote_average) entre esses diretores. 

![Diretores](/docs/img/diretores_grafico.png)

A análise desses dados revela uma distinção clara entre diretores renomados e não renomados. Diretores renomados (aqueles que dirigiram dois ou mais filmes), representando 68,7% do total e correspondendo a 3298 filmes, com uma média de avaliação (vote_average) de 6,30. Em contrapartida, os diretores não renomados (aqueles que dirigiram apenas um filme), totalizando 31,3% e com 1505 filmes e uma média de avaliação de 5,64.

Com isso conclui-se diretores renomados tendem a ter mais oportunidade dirigindo mais filmes e com uma ligeira diferença de 0,66 na média de avaliação sugerindo que os diretores renomados tendem a receber notas um pouco melhores em seus filmes. 

### Hipótese: Diretores com Orçamento Acima da Média e suas Notas ###

Diretores que trabalham com orçamentos acima da média tendem a receber notas mais altas em seus filmes?

Nesta análise, examinamos a relação entre o orçamento dos filmes e suas respectivas médias de avaliação (vote_average), focando em diretores que trabalham com orçamentos superiores à média, que é de aproximadamente 19,17 milhões.

![Orçamento e Votos](/docs/img/budget_media.png)

A análise revelou que 706 diretores possuem orçamento acima da média, o que representa cerca de 30% do total de 2.349 diretores no dataset. A média de avaliação (vote_average) para os filmes dirigidos por esses diretores é de 6,19.

Conclui-se que a relação entre orçamento e notas é positiva, embora existam filmes com altos orçamentos que não atingem avaliações excepcionais, produções com investimentos mais altos em produções cinematográficas podem levar a resultados mais favoráveis nas avaliações.


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
