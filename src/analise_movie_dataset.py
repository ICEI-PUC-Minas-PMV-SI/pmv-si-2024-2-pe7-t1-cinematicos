import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv('data/movie_dataset.csv', encoding='utf-8')

#df['vote_count'] = df['vote_count'].astype(float)

descriptive_stats = df[['vote_average', 'vote_count', 'budget', 'popularity', 'revenue']].describe()

# moda
moda_avaliacao = df['vote_average'].mode()[0]
moda_votos = df['vote_count'].mode()[0]
moda_orcamento = df['budget'].mode()[0]
moda_popularidade = df['popularity'].mode()[0]
moda_receita = df['revenue'].mode()[0]

print("Estatísticas Descritivas: \n", descriptive_stats)
print("Moda Rating: ", moda_avaliacao)
print("Moda Votos: ", moda_votos)
print("Moda Orçamento: ", moda_orcamento)
print("Moda Popularidade: ", moda_popularidade)
print("Moda Receita: ", moda_receita)





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

# plt.tight_layout()
# plt.show()

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

# plt.tight_layout()
# plt.show()

# # Correlação

correlacao_pandas = df['vote_average'].corr(df['vote_count'])
print(f"Correlação entre Média de Votos e Total de Votos: {correlacao_pandas}")

correlacao_pandas = df['vote_average'].corr(df['budget'])
print(f"Correlação entre Média de Votos e Orçamento do Filme: {correlacao_pandas}")

correlacao_pandas = df['vote_average'].corr(df['popularity'])
print(f"Correlação entre Média de Votos e Popularidade do Filme: {correlacao_pandas}")

correlacao_pandas = df['vote_average'].corr(df['revenue'])
print(f"Correlação entre Média de Votos e Lucratividade do Filme: {correlacao_pandas}")

correlacao_pandas = df['vote_count'].corr(df['popularity'])
print(f"Correlação entre Número de Votos e Popularidade do Filme: {correlacao_pandas}")

correlacao_pandas = df['popularity'].corr(df['budget'])
print(f"Correlação entre Popularidade e Orçamento do Filme: {correlacao_pandas}")

correlacao_pandas = df['revenue'].corr(df['budget'])
print(f"Correlação entre Lucro e Orçamento do Filme: {correlacao_pandas}")

correlacao_pandas = df['revenue'].corr(df['popularity'])
print(f"Correlação entre Lucro e Popularidade: {correlacao_pandas}")





# # Gráfico de dispersão entre rating e votes
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='vote_count', y='vote_average', data=df)
# plt.xscale('log')
# plt.title('Dispersão entre Votes e Rating')
# plt.xlabel('vote_count')
# plt.ylabel('vote_average')
# plt.show()