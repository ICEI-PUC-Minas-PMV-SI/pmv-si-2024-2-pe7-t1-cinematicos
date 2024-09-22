
import pandas as pd

df = pd.read_csv('movie_dataset.csv', encoding='utf-8')

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




