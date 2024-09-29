import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv('src/movie_dataset.csv', encoding='utf-8')


############################# Estastísticas Descritivas #############################

# # Carregar o dataset


# #df['vote_count'] = df['vote_count'].astype(float)

# descriptive_stats = df[['vote_average', 'vote_count', 'budget', 'popularity', 'revenue']].describe()

# # moda
# moda_avaliacao = df['vote_average'].mode()[0]
# moda_votos = df['vote_count'].mode()[0]
# moda_orcamento = df['budget'].mode()[0]
# moda_popularidade = df['popularity'].mode()[0]
# moda_receita = df['revenue'].mode()[0]

# print("Estatísticas Descritivas: \n", descriptive_stats)
# print("Moda Rating: ", moda_avaliacao)
# print("Moda Votos: ", moda_votos)
# print("Moda Orçamento: ", moda_orcamento)
# print("Moda Popularidade: ", moda_popularidade)
# print("Moda Receita: ", moda_receita)


############################# HISTOGRAMAS #############################


# sns.set_theme(style="whitegrid")

# # Histograma para 'vote_average'
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# sns.histplot(df['vote_average'].dropna(), kde=True, bins=30, color='blue')
# plt.title('Distribuição de Ratings')

# # Histograma para 'vote_count'
# plt.subplot(1, 2, 2)
# sns.histplot(df['vote_count'].dropna(), kde=True, bins=30, color='green')
# plt.title('Distribuição de Votos')
# plt.xscale('log')

# # Histograma para 'budget'
# plt.figure(figsize=(18, 9))

# plt.subplot(2, 2, 1)
# sns.histplot(df['budget'].dropna(), kde=True, bins=30, color='purple')
# plt.title('Distribuição de Budget')
# plt.xscale('log')

# # Histograma para 'popularity'
# plt.subplot(2, 2, 2)
# sns.histplot(df['popularity'].dropna(), kde=True, bins=30, color='orange')
# plt.title('Distribuição de Popularidade')

# # Histograma para 'revenue'
# plt.subplot(2, 2, 3)
# sns.histplot(df['revenue'].dropna(), kde=True, bins=30, color='red')
# plt.title('Distribuição de Receita')
# plt.xscale('log')

# plt.tight_layout()
# plt.show()


############################# BOX PLOTS #############################

# # Box plot para 'vote_average'
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# sns.boxplot(y=df['vote_average'], color='blue')
# plt.title('Box plot de Ratings')

# # Box plot para 'vote_count'
# plt.subplot(1, 2, 2)
# sns.boxplot(y=df['vote_count'], color='green')
# plt.title('Box plot de Votos')
# plt.yscale('log')

# # Box plot para 'budget'
# plt.figure(figsize=(18, 9))

# plt.subplot(2, 2, 1)
# sns.boxplot(y=df['budget'], color='purple')
# plt.title('Box plot de Budget')
# plt.yscale('log')

# # Box plot para 'popularity'
# plt.subplot(2, 2, 2)
# sns.boxplot(y=df['popularity'], color='orange')
# plt.title('Box plot de Popularidade')

# # Box plot para 'revenue'
# plt.subplot(2, 2, 3)
# sns.boxplot(y=df['revenue'], color='red')
# plt.title('Box plot de Receita')
# plt.yscale('log')

# plt.tight_layout()
# plt.show()

############################# CORRELAÇÕES #############################

# correlacao_pandas = df['vote_average'].corr(df['vote_count'])
# print(f"Correlação entre Média de Votos e Total de Votos: {correlacao_pandas}")

# correlacao_pandas = df['vote_average'].corr(df['budget'])
# print(f"Correlação entre Média de Votos e Orçamento do Filme: {correlacao_pandas}")

# correlacao_pandas = df['vote_average'].corr(df['popularity'])
# print(f"Correlação entre Média de Votos e Popularidade do Filme: {correlacao_pandas}")

# correlacao_pandas = df['vote_average'].corr(df['revenue'])
# print(f"Correlação entre Média de Votos e Lucratividade do Filme: {correlacao_pandas}")

# correlacao_pandas = df['vote_count'].corr(df['popularity'])
# print(f"Correlação entre Número de Votos e Popularidade do Filme: {correlacao_pandas}")

# correlacao_pandas = df['popularity'].corr(df['budget'])
# print(f"Correlação entre Popularidade e Orçamento do Filme: {correlacao_pandas}")

# correlacao_pandas = df['revenue'].corr(df['budget'])
# print(f"Correlação entre Lucro e Orçamento do Filme: {correlacao_pandas}")

# correlacao_pandas = df['revenue'].corr(df['popularity'])
# print(f"Correlação entre Lucro e Popularidade: {correlacao_pandas}")


############################# GRAFICOS DE DISPERSÃO #############################


# plt.figure(figsize=(18, 12))

# # Dispersão entre vote_count e vote_average
# plt.subplot(3, 3, 1)
# sns.scatterplot(x='vote_count', y='vote_average', data=df)
# plt.xscale('log')
# plt.title('Dispersão entre Votes e Rating')
# plt.xlabel('Número de Votos')
# plt.ylabel('Média de Votos')

# # Dispersão entre budget e vote_average
# plt.subplot(3, 3, 2)
# sns.scatterplot(x='budget', y='vote_average', data=df)
# plt.xscale('log')
# plt.title('Dispersão entre Orçamento e Rating')
# plt.xlabel('Orçamento')
# plt.ylabel('Média de Votos')

# # Dispersão entre popularity e vote_average
# plt.subplot(3, 3, 3)
# sns.scatterplot(x='popularity', y='vote_average', data=df)
# plt.title('Dispersão entre Popularidade e Rating')
# plt.xlabel('Popularidade')
# plt.ylabel('Média de Votos')

# # Dispersão entre revenue e vote_average
# plt.subplot(3, 3, 4)
# sns.scatterplot(x='revenue', y='vote_average', data=df)
# plt.xscale('log')
# plt.title('Dispersão entre Receita e Rating')
# plt.xlabel('Receita')
# plt.ylabel('Média de Votos')

# # Dispersão entre vote_count e popularity
# plt.subplot(3, 3, 5)
# sns.scatterplot(x='vote_count', y='popularity', data=df)
# plt.xscale('log')
# plt.title('Dispersão entre Número de Votos e Popularidade')
# plt.xlabel('Número de Votos')
# plt.ylabel('Popularidade')

# # Dispersão entre budget e popularity
# plt.subplot(3, 3, 6)
# sns.scatterplot(x='budget', y='popularity', data=df)
# plt.xscale('log')
# plt.title('Dispersão entre Orçamento e Popularidade')
# plt.xlabel('Orçamento')
# plt.ylabel('Popularidade')

# # Dispersão entre budget e revenue
# plt.subplot(3, 3, 7)
# sns.scatterplot(x='budget', y='revenue', data=df)
# plt.xscale('log')
# plt.yscale('log')
# plt.title('Dispersão entre Orçamento e Receita')
# plt.xlabel('Orçamento')
# plt.ylabel('Receita')

# # Dispersão entre popularity e revenue
# plt.subplot(3, 3, 8)
# sns.scatterplot(x='popularity', y='revenue', data=df)
# plt.xscale('log')
# plt.yscale('log')
# plt.title('Dispersão entre Popularidade e Receita')
# plt.xlabel('Popularidade')
# plt.ylabel('Receita')

# plt.tight_layout()
# plt.show()


############################# VERIFICAÇÃO DE VARIÁVEIS ZERADAS  #############################


# # Contar quantos registros têm valor 0 para todas as colunas numéricas do dataset
# zeros_por_coluna = {coluna: (df[coluna] == 0).sum() for coluna in df.columns if df[coluna].dtype != 'object'}

# print("### Quantidade de Valores 0 por Coluna ###")
# for coluna, zeros in zeros_por_coluna.items():
#     print(f"{coluna}: {zeros}")


############################# GRÁFICO MAPA DE CALOR  #############################

# colunas_selecionadas = ['budget', 'popularity', 'revenue', 'vote_average', 'vote_count']

# df_selecionado = df[colunas_selecionadas]

# correlacao = df_selecionado.corr()

# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao, annot=True, cmap='coolwarm', linewidths=0.5)

# plt.title('Mapa de Calor - Correlação entre Variáveis')

# plt.show()

# ############################# GRÁFICO DE HIPOTESE PARA DIRETORES RENOMADOS E NÃO RENOMADOS #############################


# # Criar uma coluna para contar o número de filmes por diretor
# df['director_count'] = df.groupby('director')['director'].transform('count')

# # Classificar diretores em renomados e não renomados
# df['renomado'] = df['director_count'].apply(lambda x: 'Renomado' if x >= 2 else 'Não Renomado')

# # Calcular a média de vote_average por grupo
# media_por_grupo = df.groupby('renomado')['vote_average'].mean().reset_index()

# # Contar a quantidade de filmes por grupo
# quantidade_por_grupo = df['renomado'].value_counts().reset_index()
# quantidade_por_grupo.columns = ['renomado', 'quantidade']

# # Unir as informações de média e quantidade
# resultado = pd.merge(quantidade_por_grupo, media_por_grupo, on='renomado')

# # Criar o gráfico de rosca
# plt.figure(figsize=(8, 6))  # Tamanho do gráfico menor
# # Alterar as cores para azul claro e azul menos claro
# plt.pie(resultado['quantidade'], labels=resultado['renomado'], autopct='%1.1f%%', startangle=140, colors=['#ADD8E6', '#4682B4'])

# # Criar um círculo branco no meio para formar um gráfico de rosca
# centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)

# # Adicionar detalhes no gráfico
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
# plt.title('Proporção de Diretores Renomados e Não Renomados', fontsize=14, pad=20)  # Adiciona um padding

# # Organizar informações na legenda à esquerda
# plt.subplots_adjust(left=0.3)  # Aumenta o espaço à esquerda
# for i in range(len(resultado)):
#     plt.text(-1.5, 0.6 - (i * 0.15), 
#              f"{resultado['renomado'][i]}:\nMédia de Avaliação: {resultado['vote_average'][i]:.2f}\nQuantidade de Filmes: {resultado['quantidade'][i]}",
#              horizontalalignment='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# plt.tight_layout()
# plt.show()

# # ############################# GRÁFICO DE DISPERÇÃO PARA HIPÓTESES DE ORÇAMENTO COM DIRETORES #############################

# Calcular a média do orçamento
media_budget = df['budget'].mean()

# Filtrar filmes com orçamento acima da média
df_filtrado = df[df['budget'] > media_budget]

# Calcular quantos diretores têm orçamento acima da média e a média das notas
num_diretores = df_filtrado['director'].nunique()
media_notas = df_filtrado['vote_average'].mean()

# Criar o gráfico de dispersão
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df_filtrado['budget'], df_filtrado['vote_average'], 
                      c=df_filtrado['vote_average'], cmap='viridis', alpha=0.7, edgecolors='w')

# Adicionar uma barra de cores
cbar = plt.colorbar(scatter)
cbar.set_label('Média de Avaliação', rotation=270, labelpad=15)

# Adicionar título e rótulos
plt.title('Relação entre Orçamento e Média de Avaliação dos Filmes\n(Diretores com Orçamento Acima da Média)', fontsize=16)
plt.xlabel('Orçamento (em milhões)', fontsize=14)
plt.ylabel('Média de Avaliação (vote_average)', fontsize=14)

# Definir limites para o eixo x
min_budget = media_budget
max_budget = df['budget'].max()

# Valores a serem exibidos
budget_values = np.linspace(min_budget, max_budget, num=7)

# Adicionar orçamentos na parte inferior do gráfico
for budget in budget_values:
    plt.text(budget, -0.5, f"{int(budget / 1e6)}M", 
             fontsize=10, horizontalalignment='center')

# Adicionar informações sobre diretores e média das notas na parte inferior
plt.figtext(0.5, 0.01, f"Número de Diretores: {num_diretores}   |   Média das Notas: {media_notas:.2f}",
            fontsize=12, ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=0.5'))

# Melhorar a visualização do eixo x
plt.xscale('linear')  # Usar escala linear para melhor visualização
plt.grid(True)
plt.tight_layout()
plt.ylim(-1, 10)  # Limita o eixo y para melhorar a visualização
plt.show()
