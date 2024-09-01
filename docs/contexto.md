## Introdução

 O cinema é uma das formas de entretenimento mais influentes e lucrativas do mundo moderno, com a indústria global produzindo milhares de filmes anualmente. No entanto, prever o sucesso de um filme é um desafio complexo devido à diversidade de produções e à imprevisibilidade das reações do público. Essa incerteza representa um risco significativo para produtores e investidores, que buscam maneiras eficazes de avaliar o potencial de sucesso de um filme antes de seu lançamento.
Este projeto propõe a utilização de técnicas de aprendizado de máquina para estimar com boa precisão a nota média de filmes no IMDb, uma das principais plataformas de avaliação cinematográfica mundial. O IMDb fornece uma variedade de informações sobre filmes, incluindo gênero, elenco e sinopse, bem como avaliações dos espectadores, que são fundamentais para a aceitação crítica e popular. Ao analisar esses dados, o projeto visa identificar quais características dos filmes são mais indicativas das avaliações finais. Desenvolvendo modelos preditivos, o objetivo é oferecer aos produtores e investidores uma ferramenta para tomar decisões mais informadas sobre quais projetos têm maior potencial de sucesso. Essa capacidade de previsão não apenas melhora a alocação de recursos e a estratégia de marketing, mas também contribui para um mercado cinematográfico mais estratégico e eficiente. Integrando inteligência de dados no processo de produção e promoção, esperamos otimizar o desenvolvimento de filmes e maximizar seu impacto e rentabilidade no competitivo cenário atual.

## Problema

 A imprevisibilidade das avaliações no IMDb representa um desafio significativo para a indústria cinematográfica, especialmente quando se trata de alocar recursos e definir estratégias de marketing. Identificar como as características gênero, elenco, sinopse, ano de lançamento e avaliações dos espectadores influenciam a nota média, permite que as produtoras tomem decisões mais informadas e estratégicas, otimizando suas operações e maximizando o potencial de sucesso dos filmes. O uso de técnicas de aprendizado de máquina para analisar e prever as avaliações pode proporcionar uma vantagem competitiva ao melhorar a eficiência na produção e promoção de filmes.
 
## Questão de pesquisa

 É possível que as características gênero, elenco, sinopse, ano de lançamento e as avaliações dos espectadores dos filmes sejam usadas para prever com uma boa precisão a nota média no IMDb utilizando técnicas de aprendizado de máquina?

## Objetivos preliminares

Experimentar modelos de aprendizado de máquina adequados capazes de prever a nota média de um filme no IMDb com base em um conjunto de características extraídas do dataset. 


#### Antecipar o Sucesso dos Filmes: 

Facilitar decisões estratégicas tornando a tomada de decisão mais informada sobre quais filmes têm maior potencial de sucesso .

#### Identificar Características que Maximizam a Nota Média dos Filmes

Otimizar o desenvolvimento de filmes identificando quais elementos são mais valorizados pelo público melhorando assim a qualidade e o apelo dos filmes produzidos

## Justificativa

O cinema, uma das formas de entretenimento mais influentes e lucrativas, enfrenta desafios significativos na previsão do sucesso de filmes devido à sua complexidade e à variabilidade das reações do público (Vogel, 2014). Prever o sucesso de um filme é crucial para a indústria cinematográfica, que movimenta bilhões anualmente (Gower Street Analytics, 2023). Estudos têm mostrado que características intrínsecas, como gênero, elenco, diretor e sinopse, são preditores significativos do sucesso de um filme. Um exemplo é o estudo de Eliashberg et al. (2000), que sugere que características como elenco e diretor, combinadas com o gênero, podem ser usadas para prever o desempenho de um filme em termos de receita de bilheteira.
Um exemplo recente que ilustra a importância da análise preditiva é o filme "The Flash" (2023). Com um orçamento estimado em cerca de 200 milhões de dólares e uma extensa campanha de marketing, "The Flash" foi um dos lançamentos mais esperados do ano. Apesar das expectativas, o filme não alcançou o sucesso esperado nas bilheteiras, arrecadando aproximadamente 270 milhões de dólares mundialmente, o que foi abaixo das projeções e resultou em prejuízos financeiros significativos para a Warner Bros. Esse resultado decepcionante poderia ter sido antecipado e, possivelmente, evitado com o uso de análise preditiva.

## Público-Alvo

+ ### Produtores de Filmes

| **Conhecimentos Prévios**  | Experiência em produção cinematográfica e conhecimento sobre o mercado de entretenimento. Podem ter alguma familiaridade com análise de dados, mas não necessariamente com aprendizado de máquina. |
|-----------------------|---------------------------------------------------------------------------------------------|
| **Relação com a Tecnologia** | Utilizam ferramentas digitais para planejamento e análise de mercado, mas podem não estar profundamente envolvidos em análises avançadas de dados. |
| **Relações Hierárquicas**   | Geralmente têm a última palavra sobre decisões criativas e orçamentárias. Buscam informações que ajudem a maximizar o retorno sobre o investimento. |

+ ### Executivos de Estúdios

| **Conhecimentos Prévios**  | Conhecimento extensivo sobre a indústria do cinema e experiência em gerenciamento de estúdios. Têm interesse em dados de mercado e tendências. |
|-----------------------|---------------------------------------------------------------------------------------------|
| **Relação com a Tecnologia** | Utilizam relatórios analíticos e podem usar ferramentas de análise de dados, mas o uso de técnicas avançadas de aprendizado de máquina pode ser limitado.|
| **Relações Hierárquicas**   | Responsáveis por tomar decisões estratégicas e orçamentárias, precisam de previsões precisas para alocar recursos e definir estratégias de marketing. |

+ ### Profissionais de Marketing Cinematográfico

| **Conhecimentos Prévios**  | Experiência em campanhas de marketing para filmes e compreensão das dinâmicas de promoção no setor de entretenimento. |
|-----------------------|---------------------------------------------------------------------------------------------|
| **Relação com a Tecnologia** | Usam dados e análises para planejar campanhas, mas podem não ter experiência direta com técnicas avançadas de aprendizado de máquina. |
| **Relações Hierárquicas**   | Envolvidos na criação e execução de estratégias de marketing. Buscam previsões precisas para otimizar campanhas e ajustar estratégias de promoção. |


+ ### Investidores e Financiadores

| **Conhecimentos Prévios**  | Entendem os fundamentos da indústria cinematográfica e os riscos associados ao investimento em filmes. |
|-----------------------|---------------------------------------------------------------------------------------------|
| **Relação com a Tecnologia** | Usam dados financeiros e relatórios para tomar decisões de investimento, mas não necessariamente técnicas de aprendizado de máquina. |
| **Relações Hierárquicas**   | Tomam decisões sobre alocação de investimentos e precisam de previsões confiáveis para minimizar riscos e maximizar retornos. |

*************

## Diagrama de Personas



### 1. Produtor de Filmes

- **Nome:** Alice, a Produtora

- **Idade:** 45 anos

- **Conhecimentos Prévios:** Produção de filmes, mercado cinematográfico.

- **Relação com a Tecnologia:** Utiliza ferramentas de planejamento e análise de mercado.

- **Objetivos:** Maximizar retorno sobre o investimento, tomar decisões criativas e orçamentárias.



### 2. Executivo de Estúdio

- **Nome:** Bob, o Executivo

- **Idade:** 50 anos

- **Conhecimentos Prévios:** Gestão de estúdios, estratégia de mercado.

- **Relação com a Tecnologia:** Utiliza relatórios analíticos e ferramentas de dados.

- **Objetivos:** Tomar decisões estratégicas, alocar recursos e definir estratégias de marketing.



### 3. Profissional de Marketing

- **Nome:** Carol, a Marketeira

- **Idade:** 35 anos

- **Conhecimentos Prévios:** Campanhas de marketing para filmes, promoções.

- **Relação com a Tecnologia:** Utiliza dados e análises para campanhas.

- **Objetivos:** Otimizar campanhas de marketing, ajustar estratégias promocionais.



### 4. Investidor

- **Nome:** David, o Investidor

- **Idade:** 55 anos

- **Conhecimentos Prévios:** Investimentos na indústria cinematográfica, análise de risco.

- **Relação com a Tecnologia:** Analisa dados financeiros e relatórios.

- **Objetivos:** Minimizar riscos, maximizar retornos.

  ************

  ## Mapa de Stakeholders

| Stakeholder                 | Interesse                                       | Influência       | Necessidade de Informação       |
|-----------------------------|-------------------------------------------------|------------------|--------------------------------|
| **Produtores de Filmes**    | Maximizar retorno sobre investimento, decisões criativas e orçamentárias | Alta             | Previsões de avaliações, impacto de características no sucesso |
| **Executivos de Estúdios** | Tomar decisões estratégicas e alocar recursos | Alta             | Previsões de sucesso, análise de tendências de mercado       |
| **Profissionais de Marketing** | Otimizar campanhas de marketing, ajustar estratégias promocionais | Média            | Previsões de sucesso, impacto de características no marketing  |
| **Investidores**            | Minimizar riscos e maximizar retornos          | Alta             | Previsões de sucesso financeiro, análise de riscos e oportunidades |

## Estado da arte

A previsão do sucesso de filmes e das avaliações que estes recebem é um campo crescente de interesse que se beneficia cada vez mais das técnicas de aprendizado de máquina e mineração de dados. Este campo busca entender e prever como características específicas dos filmes influenciam sua recepção crítica e popularidade, utilizando métodos estatísticos e algoritmos complexos para analisar grandes volumes de dados.

Diversos estudos têm explorado como diferentes métodos podem prever com precisão a popularidade e a recepção crítica de filmes, revelando uma variedade de abordagens e descobertas. A aplicação de técnicas de aprendizado de máquina, por exemplo, tem mostrado resultados promissores na previsão das avaliações de filmes. Bristi, Zaman e Sultana (2019) aplicaram algoritmos como redes neurais artificiais e máquinas de vetores de suporte (SVM) para prever as notas dos filmes no IMDb. Os resultados mostraram que as redes neurais artificiais oferecem a melhor precisão, seguidas por SVM e regressão linear, evidenciando como a análise de características detalhadas dos filmes, como gênero e elenco, pode melhorar a precisão das previsões.

Comparações de diferentes métodos também têm sido uma área de foco significativo. Dhir e Raj (2018) realizaram seus estudos sobre dados do IMDb, analisando diversos algoritmos de aprendizado de máquina, incluindo árvores de decisão, k-vizinhos mais próximos (k-NN) e métodos ensemble como Random Forest, para prever o sucesso de filmes, medido através de receitas e críticas. Este estudo destacou que métodos ensemble, como Random Forest, superam métodos individuais, demonstrando a eficácia desses métodos em capturar a complexidade dos dados relacionados ao sucesso dos filmes.  Os autores se propuseram a prever o quão bem-sucedido um filme seria em sua pontuação no IMDb antes de sua chegada às bilheterias. Na análise exploratória, foi apontado que o número de usuários votantes, o número de críticos para avaliações, o número de curtidas no Facebook, a duração do filme e a coleção bruta de filmes afetam a pontuação do IMDb fortemente. Filmes de drama e biográficos foram os melhores pontuados entre os gêneros.

A previsão da popularidade dos filmes foi investigada por Afzal e Latif (2016), que utilizaram técnicas de aprendizado de máquina, incluindo regressão logística e redes neurais profundas. A pesquisa mostrou que a combinação de características como gênero, marketing e elenco é crucial para prever a popularidade, com redes neurais profundas demonstrando a maior precisão. O trabalho foi realizado sobre um dataset que considera filmes lançados no período compreendido entre e 2004 e 2014. Os dados foram extraídos pelos autores diretamente do IMDB. O estudo avaliou os seguintes classifiers: Logistic Regression, Simple Logistic, Multilayer Perceptron, J48, Naive Bayes e PART. Como resultado, a mais alta precisão foi alcançada com logística simples e regressão logística, 84,34% e 84,15% respectivamente, seguidos dos resultados da árvore de decisão j48, com 82,42%.

Além das abordagens de aprendizado de máquina, a mineração de dados tem contribuído significativamente para a compreensão do sucesso dos filmes. Javaria, Prakash, Amr e Buckles (2017) aplicaram técnicas de mineração de dados, como clustering e regras de associação, para identificar padrões que precedem o sucesso dos filmes. A descoberta de que grandes orçamentos e elencos renomados estão correlacionados com maior sucesso sublinha a importância desses fatores na construção de modelos preditivos.

Saraee, White e Eccleston (2018) exploraram a análise de características dos filmes usando algoritmos de clustering e análise de componentes principais (PCA). O estudo revelou que o gênero e o envolvimento de atores famosos têm um impacto significativo nas avaliações dos filmes, reforçando a ideia de que características específicas estão fortemente associadas às notas atribuídas pelos usuários.

Em síntese, a combinação de técnicas avançadas de aprendizado de máquina e mineração de dados tem demonstrado um potencial significativo para prever com precisão o sucesso e as avaliações dos filmes. A integração de métodos como redes neurais, Random Forest e técnicas de clustering permite uma compreensão mais aprofundada dos fatores que influenciam a recepção crítica e a popularidade dos filmes. Estes avanços oferecem insights valiosos para este trabalho, que pode se valer de indicadores de algoritmos melhor sucedidos para limitar o escopo da presente pesquisa.

# Descrição do _dataset_ selecionado

O dataset escolhido foi [IMDB Dataset](https://www.kaggle.com/datasets/payamamanat/imbd-dataset/data).

Este conjunto de dados oferece uma visão abrangente sobre filmes e séries contendo aproximadamente 10,000 registros com 9 atributos, incluindo detalhes sobre seu título, ano de lançamento, classificação indicativa, duração, gênero, avaliação, descrição, elenco e número de votos. Abaixo, descrevemos cada atributo e suas características principais:

#### Title

* Tipo: String

* Descrição: Refere-se ao título do filme ou série.

* Valores Únicos: 7.912

* Valores Faltantes: Nenhum

* Distribuição dos Valores: A maioria dos títulos é única, com "Top Gear" sendo o título mais comum, aparecendo em 1% dos casos.



#### Year

* Tipo: String

* Descrição: Ano de lançamento do filme ou série.

* Valores Únicos: 498

* Valores Faltantes: 527 (5%)

* Distribuição dos Valores: O ano mais comum é 2020, que representa 7% dos registros. Há uma grande quantidade de registros com valores "Other" (8653), que podem incluir dados ausentes ou não especificados.



#### Certificate

* Tipo: String

* Descrição: Classificação indicativa (certificado) do filme ou série.

* Valores Únicos: 20

* Valores Faltantes: 3.453 (35%)

* Distribuição dos Valores: A classificação mais comum é TV-MA, que representa 25% dos registros. Há uma quantidade significativa de valores ausentes ou não especificados (35%).



#### Duration

* Tipo: String

* Descrição: Duração do filme ou série.

* Valores Únicos: 291

* Valores Faltantes: 2.036 (20%)

* Distribuição dos Valores: O valor mais comum é "60 min," representando 4% dos registros. Há muitos registros com valores "Other" (76%), sugerindo que a duração pode não ser uniformemente especificada.



#### Genre

* Tipo: String

* Descrição: Gênero do filme ou série.

* Valores Únicos: 569

* Valores Faltantes: 73 (1%)

* Distribuição dos Valores: O gênero mais comum é Comedy, que representa 9% dos registros. A maior parte dos registros é categorizada como "Other" (85%).



#### Rating

* Tipo: Decimal

* Descrição: Avaliação ou nota do filme ou série.

* Valores Únicos: Quantidade variável de avaliações em intervalos definidos.

* Valores Faltantes: 1.173 (12%)

* Distribuição dos Valores: A média das avaliações é 6.76, com a maioria das avaliações entre 6.62 e 7.44. A distribuição é bastante ampla, com um desvio padrão de 1.21, indicando variação nas avaliações.



#### Description

* Tipo: String

* Descrição: Descrição do filme ou série.

* Valores Únicos: 9.433

* Valores Faltantes: Nenhum

* Distribuição dos Valores: A maioria dos registros é "Other" (95%), indicando que a maioria dos registros não tem uma descrição específica ou padronizada.



#### Stars

* Tipo: String (lista de nomes)

* Descrição: Nomes dos principais atores ou estrelas do filme ou série.

* Valores Únicos: 8.615

* Valores Faltantes: Nenhum

* Distribuição dos Valores: A maioria dos registros tem uma lista vazia para estrelas (4%), e a maior parte dos registros é categorizada como "Other" (95%).



#### Votes

* Tipo: Decimal

* Descrição: Número de votos ou avaliações que o filme ou série recebeu.

* Valores Únicos: Quantidade variável de votos em intervalos definidos.

* Valores Faltantes: 1.173 (12%)

* Distribuição dos Valores: O número médio de votos é 19.5k, com grande variação e um desvio padrão de 87.6k, mostrando uma grande quantidade de votos recebidos.



#### Resumo dos Atributos:

* String: title, year, certificate, duration, genre, description, stars

* Decimal: rating, votes

* Valores Faltantes: Presença de valores faltantes em year, certificate, duration, rating, e votes.

* Distribuição: Existem várias categorias de dados com alta concentração de valores "Other" ou valores ausentes


# Canvas analítico

1. Questão:
O que queremos saber sobre o software/processos/uso/organização/etc?

Queremos prever a nota média de um filme no IMDb utilizando técnicas de aprendizado de máquina baseadas em características específicas, como gênero, elenco, sinopse, ano de lançamento e avaliações dos espectadores. A previsão dessa nota ajudará a entender quais fatores são mais influentes no sucesso de um filme em termos de aceitação crítica e popular. Buscamos também identificar como essas características podem ser utilizadas para melhorar a tomada de decisões na produção e promoção de filmes, maximizando o retorno sobre o investimento.

2. Data Sources:
Que dados podem possivelmente responder nossa pergunta? Que informações precisamos?

Para responder a nossa pergunta, usaremos o IMDb Dataset, que contém aproximadamente 10.000 registros com os seguintes atributos:

Título: Nome do filme ou série.
Ano de Lançamento: Ano em que o filme ou série foi lançado.
Certificado: Classificação indicativa (ex.: TV-MA, PG-13).
Duração: Tempo de execução do filme ou série.
Gênero: Gênero principal ou múltiplos gêneros do filme ou série (ex.: comédia, drama).
Avaliação (Rating): Nota média atribuída pelos usuários no IMDb.
Descrição (Sinopse): Breve descrição ou sinopse do filme ou série.
Elenco (Stars): Lista de atores principais.
Número de Votos (Votes): Número total de votos que o filme ou série recebeu.

3. Heuristics:
Quais hipóteses queremos fazer para simplificar a resposta da questão?

Hipótese 1: Filmes com atores renomados tendem a receber notas mais altas no IMDb.
Hipótese 2: Certos gêneros, como drama ou comédia, têm uma correlação mais forte com notas mais altas em comparação com outros gêneros.
Hipótese 3: Filmes lançados em anos recentes tendem a receber mais avaliações e, portanto, notas mais representativas.
Hipótese 4: A duração e o certificado de classificação podem ter uma influência moderada nas avaliações, refletindo preferências do público por certos tipos de filmes.
Hipótese 5: Filmes com uma descrição mais detalhada ou elaborada tendem a ter avaliações mais altas, pois isso pode refletir em um melhor desenvolvimento de enredo e produção.

4. Validation:
Quais resultados esperamos da nossa análise? Como ela é analisada e apresentada de uma maneira entendível?

Esperamos construir um modelo preditivo com uma boa precisão (idealmente acima de 80%) para prever a nota média de um filme no IMDb com base nas características selecionadas. A análise será apresentada em termos de:

Precisão do modelo: Métricas de desempenho como RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), e R² (Coeficiente de Determinação).
Importância das variáveis: Identificação de quais características têm o maior impacto nas previsões.
Visualizações gráficas: Gráficos de dispersão, matrizes de correlação e gráficos de importância de recursos para ajudar na interpretação dos resultados.
Interpretação dos resultados: Relatórios que destacam as descobertas principais e oferecem recomendações práticas para os stakeholders.

5. Implementation:
Como podemos implementar a análise passo a passo e de um jeito compreensível?

Coleta e pré-processamento dos dados: Ingestão e limpeza dos dados, tratamento de valores ausentes e transformação de atributos categóricos em formatos numéricos utilizáveis para modelos de aprendizado de máquina.
Análise exploratória de dados (EDA): Exploração de correlações entre características e a nota média, identificação de padrões, outliers e distribuição dos dados.
Divisão do dataset: Separação dos dados em conjuntos de treinamento e teste (e possivelmente validação cruzada).
Seleção e construção de modelos: Experimentação com diferentes algoritmos de aprendizado de máquina, como Regressão Linear, Random Forest, Redes Neurais e Support Vector Machines (SVM).
Treinamento e ajuste de modelos: Ajuste de hiperparâmetros para melhorar a precisão dos modelos.
Avaliação do modelo: Uso de métricas para comparar a performance dos modelos e selecionar o melhor.
Interpretação dos resultados: Análise da importância das características e visualizações dos resultados.
Comunicação dos resultados: Apresentação dos resultados e recomendações aos stakeholders.

6. Results:
Quais são os insights principais da nossa análise?

Determinação das características que mais influenciam as notas dos filmes no IMDb (por exemplo, gênero, elenco, etc.).
Identificação de padrões de sucesso (ex.: filmes de certos gêneros ou com determinados atores têm avaliações consistentemente mais altas).
Insights sobre a correlação entre o número de votos e a avaliação final do filme.
Descobertas sobre como fatores como ano de lançamento e duração influenciam a aceitação do público.

7. Next Steps:
Quais ações podemos tomar a partir dos resultados? Quem ou o que devemos nos dirigir depois?

Produtores e Executivos de Estúdios: Usar os insights para decisões estratégicas em projetos futuros, incluindo escolha de elenco, definição de gênero e estratégias de marketing.
Profissionais de Marketing Cinematográfico: Ajustar campanhas de marketing com base nas características que mais impactam a avaliação do público.
Investidores: Orientar investimentos com base em previsões mais confiáveis sobre o sucesso potencial dos filmes.
Refinamento do modelo: Continuar a ajustar o modelo com novos dados e características para melhorar a precisão.
Exploração de novas características: Incorporar dados adicionais, como orçamento de produção e informações de mídia social, para melhorar ainda mais a precisão das previsões.


> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)



# Referências

AFZAL, Hammad; LATIF, Muhammad Hassan. Prediction of Movies Popularity Using Machine Learning Techniques. IJCSNS International Journal of Computer Science and Network Security, v. 16, n. 8, ago. 2016. Disponível em: https://www.researchgate.net/publication/311913687_Prediction_of_Movies_popularity_Using_Machine_Learning_Techniques. Acesso em: 1 set. 2024.

BRISTO, Warda; ZAMAN, Zakia; SULTANA, Nishat. Predicting IMDb rating of movies by machine learning techniques. IEEE Access, v. 7, p. 79592-79603, 2019. Disponível em: https://ieeexplore.ieee.org/abstract/document/8944604. Acesso em: 28 ago. 2024.

DHIR, Rijul; RAJ, Anand. Movie Success Prediction Using Machine Learning Algorithms and Their Comparison. In: 2018 First International Conference on Secure Cyber Computing and Communication (ICSCCC). 2018. Disponível em: https://ieeexplore.ieee.org/abstract/document/8703320. Acesso em: 01 set. 2024.

ELIAISHBERG, Moshe; HAUSER, John R.; MUKHERJEE, Anindya. The motion picture industry: Critical issues and a research agenda. Journal of Marketing Research, v. 37, n. 3, p. 311-327, 2000.

GOWER STREET ANALYTICS. Cinema bilheteira global. 2023. Disponível em: https://www.gowerst.com/global-box-office-report-2023. Acesso em: 20 agosto 2024.

JAVARIA, Ahmad; PRAKASH, Duraisamy; AMR, Yousef; BUCKLES, Bill. Movie success prediction using data mining. 2017 IEEE 2nd International Conference on Cloud Computing and Big Data Analysis (ICCCBDA), p. 216-220, 2017. Disponível em: https://ieeexplore.ieee.org/abstract/document/8204173. Acesso em: 28 agosto de 2024.

MANANAT, P. IMDB Dataset. 2024. Disponível em: https://www.kaggle.com/datasets/payamamanat/imbd-dataset/data. Acesso em: 20 ago. 2024.

NOGUEIRA, G. Bilheteira. CNN Brasil, 2023. Disponível em: https://www.cnnbrasil.com.br/entretenimento/cinema-bilheteria-global-de-2023-foi-305-maior-que-a-de-2022/#:~:text=A%20ind%C3%BAstria%20cinematogr%C3%A1fica%20est%C3%A1%20em,dados%20da%20Gower%20Street%20Analytics. Acesso em: 20 ago. 2024.

SARAEE, M.; WHITE, S.; ECCLESTON, J. A data mining approach to analysis and prediction of movie ratings. WIT Transactions on Information and Communication Technologies, v. 33, p. 219-228, 2018. Disponível em: https://www.witpress.com/elibrary/wit-transactions-on-information-and-communication-technologies/33/14248. Acesso em: 28 ago. 2024.

VOGEL, Steven S. Entertainment industry economics: A guide for financial analysis. 9. ed. Cambridge: Cambridge University Press, 2014.

THE FLASH. Dir. Andy Muschietti. Warner Bros, 2023.



