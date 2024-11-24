import pandas as pd
import numpy as np
import os

# Carregar o dataset
df = pd.read_csv('src/movie_dataset.csv', encoding='utf-8')

# 1. Seleção de Colunas Relevantes
colunas_selecionadas = ['original_title', 'budget', 'revenue', 'vote_count', 'popularity', 'vote_average', 'genres']
df_filtrado = df[colunas_selecionadas]

# 2. Limpeza de Dados
# Substituir valores 0 por NaN
df_filtrado[['budget', 'revenue', 'vote_count', 'popularity']] = df_filtrado[['budget', 'revenue', 'vote_count', 'popularity']].replace(0, np.nan)

# Remover linhas com valores ausentes
df_limpo = df_filtrado.dropna()

# 3. Transformação de Variáveis Categóricas
# a) Separação dos Gêneros (extrair gêneros como lista a partir da coluna 'genres')
df_limpo['genres_list'] = df_limpo['genres'].apply(lambda x: [g.strip() for g in str(x).split(',')] if pd.notnull(x) else [])

# b) One-Hot Encoding (criar colunas binárias para cada gênero único)
generos_unicos = set(genero for sublist in df_limpo['genres_list'] for genero in sublist)
for genero in generos_unicos:
    df_limpo[genero] = df_limpo['genres_list'].apply(lambda x: 1 if genero in x else 0)

# c) Remoção de Colunas Intermediárias (remover 'genres' e 'genres_list')
df_preparado = df_limpo.drop(columns=['genres', 'genres_list'])

# Visualizar os primeiros dados
print(df_preparado.head())

# Criar o caminho para salvar o dataset na pasta 'src'
novo_caminho_csv = os.path.join('src', 'regressaolinear-movie_dataset.csv')

# Salvar o dataset preparado como um novo arquivo CSV
df_preparado.to_csv(novo_caminho_csv, index=False)
print(f"Novo arquivo salvo em: {novo_caminho_csv}")
