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



## Discussão dos resultados obtidos

- Os resultados indicam que o modelo capturou padrões importantes, mas ainda há muito espaço para melhorias. Um MSE e MAE baixos mostram que o modelo consegue fazer previsões minimamente razoáveis na média, enquanto o R² de 0.5178 revela que ainda existem fatores explicativos não capturados pelo modelo atual.  
- Foram realizados testes com alterações significativas no modelo, como na quantidade de neurônios, na função de ativação(ex: LeakyReLU), na taxa de regularização L2, no otimizador e em sua taxa de aprendizado, nos tamanhos dos lotes, inclusão/remoção do dropout, 
na métrica de 'loss' e no scaler de padronização dos dados. Considerando todos os testes realizados, as métricas em nenhum momento se apresentaram superiores aos resultados aqui apresentados.
- Os resultados mostram que a RNA é um modelo promissor para o problema de previsão de `vote_average`, mas ainda é necessário investir em ajustes de parâmetros e melhorias na engenharia de recursos para atingir uma performance mais robusta. Com base nos valores apresentados, o modelo já fornece previsões úteis, mas a explicabilidade e o desempenho podem ser aprimorados em iterações futuras.

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 

## Observações importantes

Todas as tarefas realizadas nesta etapa deverão ser registradas em formato de texto junto com suas explicações de forma a apresentar  os códigos desenvolvidos e também, o código deverá ser incluído, na íntegra, na pasta "src".

Além disso, deverá ser entregue um vídeo onde deverão ser descritas todas as etapas realizadas. O vídeo, que não tem limite de tempo, deverá ser apresentado por **todos os integrantes da equipe**, de forma que, cada integrante tenha oportunidade de apresentar o que desenvolveu e as  percepções obtidas.
