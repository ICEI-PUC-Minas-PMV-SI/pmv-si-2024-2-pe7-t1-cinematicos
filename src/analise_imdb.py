import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
file_path = 'pmv-si-2024-2-pe7-t1-cinematicos/IMDB.csv'
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do dataset para entender sua estrutura
df.head()

# Convertendo a coluna 'votes' para numérico (remover vírgulas)
df['votes'] = df['votes'].str.replace(',', '').astype(float)

# Estatísticas descritivas para colunas numéricas
descriptive_stats = df[['rating', 'votes']].describe()
descriptive_stats

# Medidas adicionais: moda
mode_rating = df['rating'].mode()[0]
mode_votes = df['votes'].mode()[0]

print("Descriptive Statistics: \n", descriptive_stats)
print("\nMode Rating: ", mode_rating)
print("Mode Votes: ", mode_votes)

# Configurações adicionais para visualizações
sns.set(style="whitegrid")

# Histograma para 'rating'
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['rating'].dropna(), kde=True, bins=30, color='blue')
plt.title('Distribuição de Ratings')

# Histograma para 'votes'
plt.subplot(1, 2, 2)
sns.histplot(df['votes'].dropna(), kde=True, bins=30, color='green')
plt.title('Distribuição de Votos')
plt.xscale('log')

plt.tight_layout()
plt.show()

# Box plot para 'rating'
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['rating'], color='blue')
plt.title('Box plot de Ratings')

# Box plot para 'votes'
plt.subplot(1, 2, 2)
sns.boxplot(y=df['votes'], color='green')
plt.title('Box plot de Votos')
plt.yscale('log')

plt.tight_layout()
plt.show()

# Matriz de correlação
correlation_matrix = df[['rating', 'votes']].corr()

# Heatmap da matriz de correlação
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlação entre Rating e Votes')
plt.show()

# Gráfico de dispersão entre rating e votes
plt.figure(figsize=(8, 6))
sns.scatterplot(x='votes', y='rating', data=df)
plt.xscale('log')
plt.title('Dispersão entre Votes e Rating')
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.show()