import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Carregar os dados
dados = pd.read_csv('src/regressaolinear-movie_dataset.csv')

# Selecionar as variáveis independentes e a dependente
X = dados[['budget', 'revenue', 'vote_count', 'popularity', 'Action', 'Adventure', 'Fantasy', 'Drama']]  # Adicione as variáveis relevantes
y = dados['vote_average']

# Dividir os dados em conjuntos de treinamento (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de regressão linear
modelo = LinearRegression()

# Treinar o modelo com os dados de treinamento
modelo.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = modelo.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Exibir os resultados
print(f'MSE (Erro Quadrático Médio): {mse:.2f}')
print(f'MAE (Erro Absoluto Médio): {mae:.2f}')
print(f'R² (Coeficiente de Determinação): {r2:.2f}')

# Exibir os coeficientes das variáveis
coeficientes = pd.DataFrame({'Variável': X.columns, 'Coeficiente': modelo.coef_})
print(coeficientes)
