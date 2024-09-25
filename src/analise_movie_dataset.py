import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/movie_dataset.csv', encoding='utf-8')


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


plt.figure(figsize=(18, 12))

# Dispersão entre vote_count e vote_average
plt.subplot(3, 3, 1)
sns.scatterplot(x='vote_count', y='vote_average', data=df)
plt.xscale('log')
plt.title('Dispersão entre Votes e Rating')
plt.xlabel('Número de Votos')
plt.ylabel('Média de Votos')

# Dispersão entre budget e vote_average
plt.subplot(3, 3, 2)
sns.scatterplot(x='budget', y='vote_average', data=df)
plt.xscale('log')
plt.title('Dispersão entre Orçamento e Rating')
plt.xlabel('Orçamento')
plt.ylabel('Média de Votos')

# Dispersão entre popularity e vote_average
plt.subplot(3, 3, 3)
sns.scatterplot(x='popularity', y='vote_average', data=df)
plt.title('Dispersão entre Popularidade e Rating')
plt.xlabel('Popularidade')
plt.ylabel('Média de Votos')

# Dispersão entre revenue e vote_average
plt.subplot(3, 3, 4)
sns.scatterplot(x='revenue', y='vote_average', data=df)
plt.xscale('log')
plt.title('Dispersão entre Receita e Rating')
plt.xlabel('Receita')
plt.ylabel('Média de Votos')

# Dispersão entre vote_count e popularity
plt.subplot(3, 3, 5)
sns.scatterplot(x='vote_count', y='popularity', data=df)
plt.xscale('log')
plt.title('Dispersão entre Número de Votos e Popularidade')
plt.xlabel('Número de Votos')
plt.ylabel('Popularidade')

# Dispersão entre budget e popularity
plt.subplot(3, 3, 6)
sns.scatterplot(x='budget', y='popularity', data=df)
plt.xscale('log')
plt.title('Dispersão entre Orçamento e Popularidade')
plt.xlabel('Orçamento')
plt.ylabel('Popularidade')

# Dispersão entre budget e revenue
plt.subplot(3, 3, 7)
sns.scatterplot(x='budget', y='revenue', data=df)
plt.xscale('log')
plt.yscale('log')
plt.title('Dispersão entre Orçamento e Receita')
plt.xlabel('Orçamento')
plt.ylabel('Receita')

# Dispersão entre popularity e revenue
plt.subplot(3, 3, 8)
sns.scatterplot(x='popularity', y='revenue', data=df)
plt.xscale('log')
plt.yscale('log')
plt.title('Dispersão entre Popularidade e Receita')
plt.xlabel('Popularidade')
plt.ylabel('Receita')

plt.tight_layout()
plt.show()
