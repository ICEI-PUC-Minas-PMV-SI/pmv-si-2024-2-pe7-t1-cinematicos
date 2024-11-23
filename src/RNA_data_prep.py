import pandas as pd

dados = pd.read_csv('data/movie_dataset.csv', encoding='utf-8')


# FILTRAGEM DADOS BRUTOS
colunas_desejadas = ['original_title', 'budget', 'revenue', 'vote_count', 'popularity', 'vote_average', 'genres']
dados_filtrados = dados[colunas_desejadas]

# Remover linhas que tenham valor 0 ou nulo em qualquer uma das colunas
dados_filtrados = dados_filtrados.replace(0, pd.NA)
dados_filtrados = dados_filtrados.dropna()


# Preparar colunas binárias de gêneros unícos
dados_filtrados['genres_list'] = dados_filtrados['genres'].str.split(" ")
df_genres = dados_filtrados['genres_list'].str.join('|').str.get_dummies()
df = pd.concat([dados_filtrados, df_genres], axis=1)
df = df.drop(['genres', 'genres_list'], axis=1)


print(df.head())

novo_caminho_csv = 'dataframe_prep_RNA.csv'
df.to_csv(novo_caminho_csv, index=False)
print(f"Novo arquivo salvo em: {novo_caminho_csv}")