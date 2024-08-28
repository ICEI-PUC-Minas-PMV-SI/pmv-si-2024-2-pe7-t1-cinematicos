## Introdução

 O cinema é uma das formas de entretenimento mais influentes e lucrativas do mundo moderno, com uma indústria global que produz milhares de filmes anualmente. No entanto, a previsão do sucesso de um filme ainda é uma tarefa complexa e incerta. Com a imensa variedade de produções e a volatilidade das respostas do público, prever como um filme será avaliado antes de seu lançamento representa um desafio significativo para os produtores e investidores.
Este projeto propõe a utilização de técnicas de aprendizado de máquina para estimar com precisão a nota média de um filme no IMDb, uma das plataformas de avaliação cinematográfica mais influentes e abrangentes globalmente. O IMDb não só oferece informações detalhadas sobre filmes, como gênero, elenco e sinopse, mas também fornece avaliações dos espectadores, que desempenham um papel fundamental na recepção de um filme.
Ao analisar uma ampla gama de dados disponíveis sobre filmes, nosso objetivo é identificar quais características são mais indicativas das avaliações finais recebidas. Com a aplicação de técnicas de aprendizado de máquina, buscamos desenvolver um modelo preditivo que possa oferecer previsões mais precisas das notas médias dos filmes.
A capacidade de prever essas avaliações pode fornecer uma vantagem competitiva significativa para as produtoras, permitindo-lhes tomar decisões mais assertivas sobre temas, gêneros e alocação de recursos. Além disso, este modelo pode auxiliar na estratégia de marketing e no planejamento financeiro, contribuindo para um mercado cinematográfico mais estratégico e eficiente. Ao integrar inteligência de dados ao processo de produção e promoção de filmes, esperamos não apenas melhorar o processo decisório, mas também maximizar o impacto e a rentabilidade das produções no competitivo cenário atual.

## Problema

 A imprevisibilidade das avaliações no IMDb representa um desafio significativo para a indústria cinematográfica, especialmente quando se trata de alocar recursos e definir estratégias de marketing. Identificar como as características gênero, elenco, sinopse, ano de lançamento e avaliações dos espectadores influenciam a nota média, permite que as produtoras tomem decisões mais informadas e estratégicas, otimizando suas operações e maximizando o potencial de sucesso dos filmes. O uso de técnicas de aprendizado de máquina para analisar e prever as avaliações pode proporcionar uma vantagem competitiva ao melhorar a eficiência na produção e promoção de filmes.
 
## Questão de pesquisa

 Como as características gênero, elenco, sinopse, ano de lançamento e as avaliações dos espectadores dos filmes podem ser usadas para prever com precisão a nota média no IMDb utilizando técnicas de aprendizado de máquina?

## Objetivos preliminares

 Experimentar modelos de aprendizado de máquina adequados capazes de prever a nota média de um filme no IMDb com base em um conjunto de características extraídas do dataset. Utilizando o dataset do IMDb como base, este projeto buscará responder quais características dos filmes (gênero, elenco, sinopse, etc.) têm maior impacto na nota final.

#### Analisar a Relevância das Características dos Filmes: 
Explorar o impacto das características dos filmes na nota média, utilizando técnicas estatísticas e de visualização.
#### Desenvolver e Validar Modelos Preditivos: 
Criar e testar modelos de aprendizado de máquina para prever a nota média dos filmes, avaliando sua precisão e escolhendo o melhor modelo.

## Justificativa

Prever o sucesso de um filme é crucial para a indústria cinematográfica, que movimenta bilhões anualmente (Gower Street Analytics, 2023). A imprevisibilidade das avaliações de filmes dificulta decisões estratégicas sobre orçamento e marketing, levando a riscos financeiros significativos.
O IMDb fornece um vasto conjunto de dados que inclui informações sobre gênero, elenco e avaliações, mas a análise tradicional desses dados não consegue prever com precisão as notas médias. Técnicas de aprendizado de máquina podem processar grandes volumes de dados e identificar padrões complexos, oferecendo previsões mais confiáveis. Este projeto busca usar aprendizado de máquina para prever as avaliações dos filmes com maior precisão. Isso pode ajudar as produtoras a tomar decisões mais informadas, otimizando recursos e estratégias de marketing, e oferecendo uma vantagem competitiva significativa no mercado cinematográfico.

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

[Predicting IMDb Rating of Movies by Machine Learning Techniques](https://ieeexplore.ieee.org/abstract/document/8944604)

[Movie Success Prediction using Machine Learning Algorithms and their Comparison](https://ieeexplore.ieee.org/abstract/document/8703320)

[Movie success prediction using data mining](https://ieeexplore.ieee.org/abstract/document/8204173)

[A Data Mining Approach To Analysis And Prediction Of Movie Ratings](https://www.witpress.com/elibrary/wit-transactions-on-information-and-communication-technologies/33/14248)

[Prediction of Movies popularity Using Machine Learning Techniques](https://www.researchgate.net/profile/Hammad-Afzal/publication/311913687_Prediction_of_Movies_popularity_Using_Machine_Learning_Techniques/links/586253ce08ae6eb871ab0748/Prediction-of-Movies-popularity-Using-Machine-Learning-Techniques.pdf)




Nesta seção, deverão ser descritas outras abordagens identificadas na literatura que foram utilizadas para resolver problemas similares ao problema em questão. Para isso, faça uma pesquisa detalhada e identifique, no mínimo, 5 trabalhos que tenham utilizado dados em contexto similares e então: (a) detalhe e contextualize o problema, (b) descreva as principais características do _dataset_ utilizado, (c) detalhe quais abordagens/algoritmos foram utilizados (e seus parâmetros), (d) identifique as métricas de avaliação empregadas, e (e) fale sobre os resultados obtidos. 

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

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

Nesta seção, você deverá estruturar o seu Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio. O Canvas Analítico deverá ser preenchido integralmente mesmo que você não tenha "tantas certezas".

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Referências
[Bilheteria](https://www.cnnbrasil.com.br/entretenimento/cinema-bilheteria-global-de-2023-foi-305-maior-que-a-de-2022/#:~:text=A%20ind%C3%BAstria%20cinematogr%C3%A1fica%20est%C3%A1%20em,dados%20da%20Gower%20Street%20Analytics)

