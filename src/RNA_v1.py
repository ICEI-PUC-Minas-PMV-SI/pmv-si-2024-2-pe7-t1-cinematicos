import pandas as pd

from sklearn.preprocessing import RobustScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dropout
from tensorflow.keras import Input
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


#Adição do EarlyFitting para evitar overfitting quando aumento o número de épocas
#Adição de camada de dropout para evitar overfitting
#Adição de Regularização L2 para penalizar pesos muito altos, reduzindo overfitting.
#Adição do otimizador Adam e com ajuste fino da taxa de aprendizado
#Adição da métrica MAE - Mean Absolute Error
#Alteração da normalização para RobustScaler, tentando lidar melhor com outliers
#Adição da Métrica r2


dados = pd.read_csv('dataframe_prep_RNA.csv', encoding='utf-8')
#PREPARAçÃO DOS DADOS PARA RNA
X = dados[['budget', 'revenue', 'vote_count', 'popularity', 'Action', 'Adventure', 'Fantasy', 'Science', 'Fiction', 'Crime', 'Drama', 'Thriller', 'Animation', 'Family', 'Western', 'Comedy', 'Romance', 'Horror', 'Mystery', 'History', 'War', 'Music', 'Documentary', 'Foreign']]
y = dados['vote_average'].values.reshape(-1, 1)
#y = dados['vote_average']   

# Padronizar os dados para que tenham média 0 e desvio padrão 1
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

y = dados['vote_average'].values.reshape(-1, 1)
y_scaler = RobustScaler()
y_scaled = y_scaler.fit_transform(y)

# ----------------

modelo = Sequential()

modelo.add(Input(shape=(X_scaled.shape[1],)))

# Primeira camada densa (input), x neurônios e função de ativação ReLU
modelo.add(Dense(32, activation='relu', kernel_regularizer=l2(0.1)))

# Dropout
#modelo.add(Dropout(0.5))

# Camada oculta com 64 neurônios e função de ativação ReLU
modelo.add(Dense(64, activation='relu'))
modelo.add(Dense(64, activation='relu'))

# Camada de saída com um neurônio (já que estamos prevendo um valor contínuo)
modelo.add(Dense(1))

# Compilar o modelo com a função de perda de erro quadrático médio (MSE) e otimizador Adam
modelo.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# ----------------


# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# Treinar a rede neural
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
modelo.fit(X_train, y_train, epochs=70, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping])


# Avaliar o modelo
loss = modelo.evaluate(X_test, y_test)
print(f'Erro quadrático médio no conjunto de teste: {loss}')

predictions = modelo.predict(X_test)
#predictions = predictions.reshape(-1)
mae = mean_absolute_error(y_test, predictions)
print(f'Erro absoluto médio no conjunto de teste: {mae}')

r2 = r2_score(y_test, predictions)
print(f'R² no conjunto de teste: {r2}')

