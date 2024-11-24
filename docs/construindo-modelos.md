# Preparação dos dados

Foram realizadas as seguintes etapas de **pré-processamento e tratamento dos dados**, alinhadas às melhores práticas para trabalhar com conjuntos de dados antes de aplicá-los em modelos de aprendizado de máquina. 

## **1. Seleção de Colunas Relevantes**
- **Técnica:** Filtragem das colunas desejadas.
- **Colunas Selecionadas:** `original_title`, `budget`, `revenue`, `vote_count`, `popularity`, `vote_average`, `genres`.
- **Objetivo:** Reduzir o conjunto de dados a apenas as variáveis relevantes para este estudo, descartando informações irrelevantes ou redundantes para o problema.

## **2. Limpeza de Dados**
- **Técnica:** Substituição de valores `0` por `NA` e remoção de linhas com valores ausentes.
- **Objetivo:**
  - Garantir que apenas entradas válidas permaneçam no conjunto de dados.
  - Excluir registros com valores que comprometem a análise, como orçamentos ou receitas iguais a zero.

## **3. Transformação de Variáveis Categóricas**

### **a) Separação dos Gêneros**
- **Técnica:** A coluna `genres` é convertida em listas de gêneros.

### **b) One-Hot Encoding**
- **Técnica:** Criar colunas binárias correspondentes a cada gênero único no dataset.
- **Exemplo:** Se a coluna `genres` contém `Action Comedy`, serão criadas colunas `Action` e `Comedy` com valores `1` ou `0` para indicar a presença ou ausência desses gêneros.
- **Objetivo:** Transformar uma variável categórica em uma representação numérica adequada para os modelos de aprendizado de máquina.

### **c) Remoção de Colunas Intermediárias**
- **Técnica:** As colunas `genres` e `genres_list`, usadas para criação das variáveis binárias, são descartadas.
- **Objetivo:** Manter apenas as colunas relevantes e evitar redundância no conjunto de dados.

## **4. Escalonamentos**
- **Técnica:**  Aplicar padronização ou normalização às variáveis numéricas.
- **Objetivo:** Garantir uniformidade entre as escalas, caso seja necessário para os algoritmos utilizados posteriormente.

# Descrição dos modelos

## **Modelo Utilizado 1: Rede Neural Artificial (RNA)**

### **Sobre:**

#### **1. Fundamentos e Princípios de Funcionamento**
Uma RNA é composta por camadas de neurônios interconectados que processam os dados de entrada, aprendendo padrões complexos para fazer previsões. Este modelo é altamente flexível e poderoso, especialmente em problemas de **regressão**, como o caso do nosso problema, onde o objetivo é prever a nota média (`vote_average`) dos filmes com base em diversos atributos.

#### **2. Vantagens**
- **Capacidade de modelar relações não lineares:** Ideal para conjuntos de dados com padrões complexos.
- **Ajuste de pesos dinâmico:** Aprendizagem iterativa com base no erro reduzido.
- **Personalização:** Capacidade de trabalhar os parâmetros mais relevantes do modelo, garantindo flexibilidade na arquitetura (número de camadas, neurônios, funções de ativação, etc.).

#### **3. Limitações**
- **Poder computacional:** Requer maior quantidade de dados e poder computacional comparado a modelos mais simples, como regressão linear.
- **Susceptibilidade a overfitting:** Por isso, medidas de regularização e estratégias como `EarlyStopping` e `Dropout` foram incorporadas.

#### **4. Justificativa da Escolha**
A RNA foi escolhida devido à complexidade do problema, que envolve dados contínuos, como orçamento e receita, além de binários (gêneros do filme). Este modelo pode capturar relações sutis e não lineares, essenciais para aumentar a precisão nas previsões.

### **Arquitetura do Modelo:**

1. **Pré-processamento dos Dados**
   - Foi utilizado o **RobustScaler**, que é robusto a outliers, para escalonar os dados de entrada (`X`) e a variável alvo (`y`).

2. **Camadas do Modelo**
   - **Entrada:** Primeira camada densa com 32 neurônios e função de ativação **ReLU**, que é eficaz em redes profundas e evita problemas de saturação de gradientes.
   - **Camadas Ocultas:** Duas camadas densas com 64 neurônios cada, também com ReLU.
   - **Regularização L2:** Penaliza pesos muito altos para evitar overfitting.
   - **Camada de Saída:** Um único neurônio sem função de ativação, apropriado para regressão.

3. **Regularização**
   - **Dropout:** Evita o sobreajuste ao desativar aleatoriamente neurônios durante o treinamento.
   - **EarlyStopping:** Monitora a perda no conjunto de validação e interrompe o treinamento ao detectar estagnação.

4. **Otimizador**
   - **Adam:** Escolhido por sua eficiência e capacidade de ajustar dinamicamente as taxas de aprendizado.

5. **Função de Perda**
   - **Erro Quadrático Médio (MSE):** Penaliza desvios maiores, sendo apropriado para regressão contínua.


## **Modelo Utilizado 2: Regressão Linear Multivariada**

### **Sobre:**

#### **1. Fundamentos e Princípios de Funcionamento**
A Regressão Linear Multivariada é um modelo estatístico que estabelece uma relação linear entre uma variável dependente (neste caso, vote_average) e uma ou mais variáveis independentes (como budget, popularity, revenue, vote_count e os gêneros de filmes representados como variáveis binárias através do one-hot encoding). O modelo assume que a variável dependente pode ser descrita como uma combinação linear ponderada das variáveis independentes mais um termo de erro.

#### **2. Vantagens**
- **Simplicidade e Interpretabilidade:** As relações entre as variáveis são representadas de maneira simples e clara, permitindo fácil interpretação dos coeficientes. Cada coeficiente indica a variação na variável dependente associada a uma variação unitária na variável independente correspondente, mantendo constantes todas as outras variáveis.
- **Baixo Custo Computacional:** Comparado a modelos mais complexos, como redes neurais, a regressão linear é eficiente em termos de processamento e memória. Isso facilita o treinamento do modelo mesmo com hardware limitado e permite uma rápida implementação.
- **Robustez para Relações Lineares:**  Ideal para identificar e modelar padrões lineares entre variáveis, sendo importante quando a relação entre as variáveis é verdadeiramente linear.
- **Generalização:** Quando está bem ajustado, o modelo de regressão linear multivariada tende a generalizar bem para novos dados, o que é crucial para sua aplicação prática em previsão e tomada de decisão.

#### **3. Limitações**
- **Incapacidade de Modelar Relações Não Lineares:** O modelo pressupõe uma relação linear entre as variáveis, podendo falhar em capturar padrões mais complexos.
- **Sensibilidade a Outliers:** Valores extremos podem distorcer os coeficientes estimados,levando a previsões imprecisas. Isso requer uma cuidadosa avaliação e, possivelmente, o tratamento de outliers antes de ajustar o modelo.
- **Multicolinearidade:** Relações fortes entre variáveis independentes podem impactar a precisão dos coeficientes e dificultar a interpretação.

#### **4. Justificativa da Escolha**
A regressão linear multivariada foi escolhida devido à sua capacidade comprovada de capturar padrões lineares entre variáveis numéricas e categóricas (após o one-hot encoding dos gêneros). Dada a natureza dos dados, que incluem tanto variáveis contínuas quanto categóricas, este modelo é apropriado para problemas de regressão contínua. É uma escolha natural para explorar e quantificar como as características dos filmes influenciam suas avaliações médias (vote_average).

#### **5. Arquitetura do Modelo**

1. **Pré-processamento dos Dados**
- Tratamento de Dados Faltantes e Outliers: remoção de registros com valores ausentes e substituição ou tratamento de valores extremos que poderiam distorcer os resultados do modelo.
- Normalização: As variáveis contínuas (budget, revenue, popularity, etc.) são escaladas para um intervalo uniforme para evitar que magnitudes diferentes impactem o modelo.

2. **Variáveis Selecionadas**
- Independentes: budget, popularity, revenue, vote_count, e indicadores binários de gêneros (Action, Drama, Comedy, etc.).
- Dependente: vote_average.

3. **Divisão dos Dados** 
- Treinamento e Teste: o conjunto de dados foi dividido em dois subconjuntos: um para treinamento (80% dos dados) e outro para teste (20% dos dados). Esta divisão permite avaliar a capacidade preditiva do modelo em dados não vistos durante o treinamento.
- Validação Cruzada: adicionalmente, pode-se utilizar técnicas de validação cruzada para assegurar que o modelo não está superajustado aos dados de treinamento e que generaliza bem para novos dados.
  
# Avaliação dos modelos criados

## **1. Modelo RNA**

### **Métricas Utilizadas**

#### **Erro Quadrático Médio (MSE)**
- **Resultado Obtido:** 0.3396  
- **Interpretação:**  
  O MSE avalia o desvio médio ao quadrado entre os valores reais e previstos. Um valor menor indica previsões mais precisas. Neste caso, o valor obtido (0.3396) mostra que, em média, os desvios entre as previsões e os valores reais são baixos, embora ainda não ideais.

#### **Erro Absoluto Médio (MAE)**
- **Resultado Obtido:** 0.4401  
- **Interpretação:**  
  O MAE mede o erro médio absoluto em termos diretos, sendo mais fácil de interpretar. No contexto do problema, o modelo erra, em média, 0.44 pontos na previsão das notas (`vote_average`), o que é relativamente aceitável dependendo da escala dos valores de saída (normalizados, neste caso).

#### **Coeficiente de Determinação (R²)**
- **Resultado Obtido:** 0.5178  
- **Interpretação:**  
  O R² mede a proporção da variância dos dados que o modelo consegue explicar. Um valor de 0.5178 indica que o modelo explica cerca de 51,78% da variabilidade nos dados de teste. Embora seja um valor razoável, ele sugere que o modelo pode ser melhorado para capturar mais padrões presentes nos dados.

## **2. Modelo Regressão Linear Multivariada**

### **Métricas Utilizadas**

#### **Erro Quadrático Médio (MSE)**
- **Resultado Obtido:** 0.59  
- **Interpretação:**  O MSE mede o desvio médio ao quadrado entre os valores reais e os previstos. Valores menores indicam maior precisão do modelo. O MSE de 0.59 mostra que há desvios razoáveis nas previsões, sugerindo que o modelo ainda não está otimizado. Embora não seja um valor extremamente alto, ainda há espaço significativo para melhorias.
  
#### **Erro Absoluto Médio (MAE)**
- **Resultado Obtido:** 0.60
- **Interpretação:**  Interpretação: O MAE representa o erro médio absoluto entre os valores reais e previstos, sendo mais interpretável por expressar desvios em valores absolutos. Com um MAE de 0.60, o modelo apresenta erros médios moderados em relação às avaliações reais dos filmes. É um desempenho que indica certa precisão, mas também reforça a necessidade de ajustes ou inclusão de mais variáveis preditoras.

#### **Coeficiente de Determinação (R²)**
- **Resultado Obtido:** 0.26
- **Interpretação:**   O R² mede a proporção da variância nos valores de saída que o modelo é capaz de explicar. Um valor de 0.26 indica que apenas 26% da variação nas notas dos filmes (vote_average) é explicada pelas variáveis preditoras incluídas no modelo. Isso sugere que o modelo atual captura apenas uma fração limitada da relação entre as variáveis independentes e dependentes, sendo necessário explorar outras variáveis ou modelos mais complexos.

### **Análise dos Coeficientes das Variáveis**
Os coeficientes representam o impacto de cada variável na previsão da nota média dos filmes (vote_average).

# Tabela de Coeficientes das Variáveis

| Variável    | Coeficiente         | Interpretação                                                                 |
|-------------|---------------------|-------------------------------------------------------------------------------|
| **budget**  | -6.263725e-09       | O orçamento tem um impacto muito pequeno e negativo na média de avaliação dos filmes. |
| **revenue** | 5.041638e-11        | A receita também possui um impacto mínimo e positivo na média de avaliação.  |
| **vote_count** | 3.287690e-04    | A contagem de votos tem uma contribuição pequena, mas positiva, para a média de avaliação. |
| **popularity** | 3.552134e-04    | A popularidade contribui positivamente para a média de avaliação, mas com um peso pequeno. |
| **Action**  | -6.509819e-01       | O gênero "Action" tem um impacto negativo significativo na média de avaliação dos filmes. |
| **Adventure** | 3.430807e-01     | O gênero "Adventure" tem um impacto positivo moderado na média de avaliação dos filmes. |
| **Fantasy** | 2.617018e-01        | O gênero "Fantasy" também contribui positivamente, mas com um peso menor que "Adventure". |
| **Drama**   | 4.877559e-01        | O gênero "Drama" possui o maior impacto positivo na média de avaliação entre os gêneros analisados. |

**Nota**: Os valores dos coeficientes representam a magnitude e a direção do impacto de cada variável no modelo de regressão linear. Coeficientes positivos indicam que um aumento na variável aumenta a média de avaliação, enquanto valores negativos indicam o contrário.

**Por Que Apenas 4 Gêneros Foram Utilizados?**
Após a análise do processamento do dataset, constatou-se que os gêneros Action, Adventure, Fantasy, e Drama foram mantidos por representarem uma parte significativa dos dados e serem frequentes no conjunto original.
Esses gêneros provavelmente foram selecionados manualmente ou com base em sua alta frequência no dataset para simplificar a análise e reduzir a complexidade do modelo. Gêneros menos frequentes ou de baixa representatividade foram descartados, o que é comum em problemas de regressão onde a inclusão de variáveis irrelevantes pode introduzir ruído e comprometer a precisão do modelo.

## Discussão dos resultados obtidos - MODELO RNA

- Os resultados indicam que o modelo capturou padrões importantes, mas ainda há muito espaço para melhorias. Um MSE e MAE baixos mostram que o modelo consegue fazer previsões minimamente razoáveis na média, enquanto o R² de 0.5178 revela que ainda existem fatores explicativos não capturados pelo modelo atual.  
- Foram realizados testes com alterações significativas no modelo, como na quantidade de neurônios, na função de ativação(ex: LeakyReLU), na taxa de regularização L2, no otimizador e em sua taxa de aprendizado, nos tamanhos dos lotes, inclusão/remoção do dropout, 
na métrica de 'loss' e no scaler de padronização dos dados. Considerando todos os testes realizados, as métricas em nenhum momento se apresentaram superiores aos resultados aqui apresentados.
- Os resultados mostram que a RNA é um modelo promissor para o problema de previsão de `vote_average`, mas ainda é necessário investir em ajustes de parâmetros e melhorias na engenharia de recursos para atingir uma performance mais robusta. Com base nos valores apresentados, o modelo já fornece previsões úteis, mas a explicabilidade e o desempenho podem ser aprimorados em iterações futuras.

## Discussão dos resultados obtidos - MODELO REGRESSÃO LINEAR
Os resultados obtidos com o modelo de regressão linear multivariada mostram que ele possui várias limitações em capturar a variabilidade nas notas médias dos filmes. Isso é evidenciado pelo baixo coeficiente de determinação 
𝑅²(0.26), que indica que apenas 26% da variação nas notas (vote_average) é explicada pelas variáveis preditoras incluídas no modelo.
O erro quadrático médio (MSE) de 0.59 sugere que há desvios razoáveis nas previsões, o que indica que o modelo ainda não está otimizado. Portanto, há espaço significativo para melhorias. Além disso, o erro absoluto médio (MAE) de 0.60 implica que o modelo erra, em média, 0.60 pontos na previsão das médias das avaliações dos filmes, o que é moderadamente aceitável, mas demonstra a necessidade de ajustes.
Além disso, a simplificação dos gêneros a apenas quatro (Action, Adventure, Fantasy e Drama) pode ter limitado a capacidade do modelo de capturar padrões mais complexos no dataset. Pode-se explorar métodos para incluir mais variáveis relevantes, como duração do filme, país de origem, ou outros gêneros, que podem potencialmente aumentar a capacidade do modelo em explicar a variabilidade nas notas dos filmes.
A análise dos coeficientes dos gêneros mostra que "Drama" tem o maior impacto positivo (0.4878), enquanto "Action" possui um impacto negativo significativo (-0.6509) na média das avaliações dos filmes, indicando que tais relações são importantes para a predição da variável dependente.
Para melhorias, podemos considerar:
- Incluir mais variáveis relevantes: Adicionar atributos adicionais pode melhorar a explicabilidade do modelo.
- Explorar interações entre variáveis: Analisar como interações entre variáveis independentes podem influenciar as previsões.
- Testar modelos mais complexos: Explorar modelos mais sofisticados como árvores de decisão ou redes neurais.

## Comparação entre os Modelos: Rede Neural Artificial (RNA) vs. Regressão Linear Multivariada
### Eficiência e Resultados
**Rede Neural Artificial (RNA)**
MSE: 0.3396
MAE: 0.4401
R²: 0.5178

**Regressão Linear Multivariada**
MSE: 0.59
MAE: 0.60
R²: 0.26

## Comparação e Discussão
Os valores das métricas de desempenho evidenciam que o modelo de RNA supera a Regressão Linear Multivariada em termos de precisão e capacidade explicativa. A RNA apresenta um MSE e MAE mais baixos, sugerindo que as previsões feitas pelo modelo de RNA são mais próximas dos valores reais. Além disso, o 
𝑅² da RNA é significativamente maior (0.5178) do que o da regressão linear (0.26), indicando que a RNA é mais eficaz em explicar a variabilidade das notas médias dos filmes.

### Vantagens e Limitações
**Vantagens da Rede Neural Artificial (RNA):**
- Capacidade de modelar relações não lineares: Ideal para conjuntos de dados com padrões complexos, que não podem ser capturados por modelos lineares.
- Flexibilidade na arquitetura: A RNA permite ajustar vários hiperparâmetros como número de camadas, neurônios por camada, funções de ativação, etc.
- Melhor desempenho preditivo: Métricas indicam uma capacidade superior de previsão.

**Limitações da Rede Neural Artificial (RNA):**
- Requer maior poder computacional: O treinamento de RNAs pode ser lento e demanda mais recursos.
- Configuração mais complexa: O ajuste de hiperparâmetros para evitar overfitting pode ser desafiador.

**Vantagens da Regressão Linear Multivariada:**
- Simplicidade e interpretabilidade: Relações entre variáveis são claras e os resultados são facilmente compreendidos.
- Baixo custo computacional: Rápida implementação e menos onerosa em termos de processamento.
- Generalização em relações lineares: Funciona bem para identificar padrões lineares, que podem ser robustos.

**Limitações da Regressão Linear Multivariada:**
- Incapacidade de capturar não linearidade: O modelo não é eficaz em identificar padrões não lineares presentes nos dados.
- Sensibilidade a outliers e multicolinearidade: Valores extremos e relações fortes entre variáveis independentes podem distorcer os resultados.

## Conclusão sobre as discussões acerca dos modelos utilizados
Ambos os modelos têm seus méritos e limitações, mas a análise das métricas de desempenho sugere que a Rede Neural Artificial (RNA) é mais eficiente para o problema em questão, oferecendo previsões mais precisas e uma melhor capacidade explicativa em relação à Regressão Linear Multivariada. Portanto, a RNA se sobressai e pode ser considerada a melhor escolha para previsão das notas médias dos filmes, especialmente devido à sua habilidade em modelar relações complexas e não lineares nos dados.
Recomenda-se investir mais em ajustes de parâmetros e melhorias na engenharia de recursos para maximizar o potencial da RNA, enquanto a Regressão Linear Multivariada poderia servir como um modelo de linha de base ou em casos onde interpretabilidade e simplicidade são mais valorizadas.

# Pipeline de Pesquisa e Análise de Dados

1. **Definição do Problema:**
   - Identificar o objetivo principal do estudo ou aplicação.
   - Definir claramente as questões de pesquisa e as metas desejadas, incluindo as métricas de sucesso para avaliação dos modelos.

2. **Levantamento e Análise da Bibliografia:**
   - Revisar a literatura existente sobre o tema para identificar abordagens e lacunas.
   - Coletar referências sobre métodos, algoritmos e métricas utilizadas.

3. **Coleta dos Dados:**
   - Obter dados de fontes confiáveis, como bases de dados públicas, APIs, sensores, ou arquivos internos.
   - Garantir que a coleta seja realizada de forma ética e em conformidade com a legislação, incluindo preocupações de privacidade de dados e conformidade com regulamentações como GDPR.

4. **Análises Exploratórias Preliminares:**
   - Realizar inspeções iniciais nos dados disponíveis, incluindo visualização de dados e estatísticas descritivas. 
   - Identificar possíveis padrões ou limitações antes de avançar.
   - Considerar a segmentação de dados para identificar subgrupos dentro dos dados.

5. **Preparação dos Dados:**
   - **Limpeza:** Tratamento de valores ausentes, inconsistências e remoção de outliers.
   - **Transformação:** Normalização, padronização, codificação de variáveis categóricas e criação de novas variáveis.

7. **Arquitetura da Solução:**
   - Desenho da estrutura geral da solução, com detalhamento dos conceitos e das ferramentas que serão utilizadas.
   - Planejamento dos modelos e técnicas a serem explorados, com justificativa.

8. **Desenvolvimento de Modelos:**
   - Seleção de algoritmos de aprendizado de máquina adequados ao problema.
   - Treinamento e validação.
   - Otimização de hiperparâmetros para melhorar o desempenho do modelo.
   - Teste de diferentes arquiteturas para comparar resultados.

9. **Interpretação e Comunicação:**
   - Geração de relatórios e visualizações para comunicar os resultados.
   - Interpretação prática dos resultados no contexto do problema.
   - Preparação para apresentação de insights ao público-alvo.

## Observações: 

- **Automação:** Sempre que possível, deve-se considerar a automação de processos que se repetem nas diversão iterações pela pipeline.
- **Flexibilidade:** O processo deve ser flexível e ajustável, permitindo revisões contínuas durante o projeto, incluindo até mesmo o regresso a etapas anteriores, quando necessário.

## Observações importantes

Todas as tarefas realizadas nesta etapa deverão ser registradas em formato de texto junto com suas explicações de forma a apresentar  os códigos desenvolvidos e também, o código deverá ser incluído, na íntegra, na pasta "src".

Além disso, deverá ser entregue um vídeo onde deverão ser descritas todas as etapas realizadas. O vídeo, que não tem limite de tempo, deverá ser apresentado por **todos os integrantes da equipe**, de forma que, cada integrante tenha oportunidade de apresentar o que desenvolveu e as  percepções obtidas.
