## Introdução

 O mundo do cinema esta em constante mudança, com produções crescentes e cada vez mais diversificadas. Uma grande vantagem é entender como o público pode reagir a um filme antes de seu lançamento. Este projeto se propõe a desenvolver um modelo que ajude a prever a nota média de um filme no IMDb, uma das principais plataformas de avaliação cinematográfica.
 O IMDb oferece uma enorme quantidade de informações sobre filmes – desde o gênero e o elenco até a sinopse e o ano de lançamento, além das avaliações dos espectadores. Ao explorar esses dados, nosso objetivo é identificar quais características têm mais influência na nota final que um filme recebe.
 Produtoras podem usar essas previsões para escolher temas e gêneros com maior potencial de sucesso, planejar orçamentos e alocar recursos de forma mais eficiente, e dessa forma contribuir para que filmes tenham um impacto mais significativo e consequentemente mais lucrativo no mercado.

## Problema

 O problema que este projeto busca resolver é a dificuldade em identificar quais características dos filmes têm o maior impacto na nota média que eles recebem. A variedade nas avaliações dos filmes torna difícil para as produtoras prever com precisão como um filme será avaliado pelos espectadores. Isso pode resultar em decisões menos informadas sobre quais filmes têm maior potencial de sucesso e como alocar recursos e esforços de marketing de forma eficaz.

## Questão de pesquisa

 Quais características de um filme são relevantes para determinar a nota média do filme no IMDB?

## Objetivos preliminares

 Experimentar modelos de aprendizado de máquina adequados capazes de prever a nota média de um filme no IMDb com base em um conjunto de características extraídas do dataset. Utilizando o dataset do IMDb como base, este projeto buscará responder quais características dos filmes (gênero, elenco, sinopse, etc.) têm maior impacto na nota final.

#### Analisar a Relevância das Características dos Filmes: 
Explorar o impacto das características dos filmes na nota média, utilizando técnicas estatísticas e de visualização.
#### Desenvolver e Validar Modelos Preditivos: 
Criar e testar modelos de aprendizado de máquina para prever a nota média dos filmes, avaliando sua precisão e escolhendo o melhor modelo.

## Justificativa

A indústria cinematográfica movimenta bilhões de dólares anualmente e exerce uma influência significativa na cultura popular. A capacidade de prever o sucesso de um filme antes de seu lançamento pode trazer diversos benefícios para a indústria.
O dataset do IMDb oferece uma rica fonte de dados sobre filmes, permitindo analisar um vasto conjunto de características e identificar padrões que podem influenciar a percepção do público. Considerando a bilheteria global de 2023, Gower Street Analytics estima que a arrecadação total do último ano foi US$ 33,9 bilhões, a otimização das decisões de investimento com base em dados pode gerar um impacto econômico significativo. 

## Público-Alvo

Descreva quem serão as pessoas que poderão se beneficiar com a sua investigação indicando os diferentes perfis. O objetivo aqui não é definir quem serão os clientes ou quais serão os papéis dos usuários na aplicação. A ideia é, dentro do possível, conhecer um pouco mais sobre o perfil dos usuários: conhecimentos prévios, relação com a tecnologia, relações hierárquicas, etc.

Adicione informações sobre o público-alvo por meio de uma descrição textual, diagramas de personas e mapa de stakeholders.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

## Estado da arte

[Predicting IMDb Rating of Movies by Machine Learning Techniques]([https://dl.acm.org/](https://ieeexplore.ieee.org/abstract/document/8944604))

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

[IMDB Dataset](https://www.kaggle.com/datasets/payamamanat/imbd-dataset/data)


Nesta seção, você deverá descrever detalhadamente o _dataset_ selecionado. Lembre-se de informar o link de acesso a ele, bem como, de descrever cada um dos seus atributos (a que se refere, tipo do atributo etc.), se existem atributos faltantes etc.

# Canvas analítico

Nesta seção, você deverá estruturar o seu Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio. O Canvas Analítico deverá ser preenchido integralmente mesmo que você não tenha "tantas certezas".

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Referências
[Bilheteria](https://www.cnnbrasil.com.br/entretenimento/cinema-bilheteria-global-de-2023-foi-305-maior-que-a-de-2022/#:~:text=A%20ind%C3%BAstria%20cinematogr%C3%A1fica%20est%C3%A1%20em,dados%20da%20Gower%20Street%20Analytics)

