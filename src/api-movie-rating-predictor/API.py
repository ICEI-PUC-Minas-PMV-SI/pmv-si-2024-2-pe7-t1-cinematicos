from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import numpy as np
import joblib

modelo_carregado = load_model('cinematicosRNA.keras')
X_scaler = joblib.load('X_scaler.pkl')
y_scaler = joblib.load('y_scaler.pkl')

class Entrada(BaseModel):
    budget: float
    revenue: float
    vote_count: float
    popularity: float
    Action: int
    Adventure: int
    Fantasy: int
    Science: int
    Fiction: int
    Crime: int
    Drama: int
    Thriller: int
    Animation: int
    Family: int
    Western: int
    Comedy: int
    Romance: int
    Horror: int
    Mystery: int
    History: int
    War: int
    Music: int
    Documentary: int
    Foreign: int

app = FastAPI()

@app.post("/prever")
async def prever(entrada: Entrada):
   
    entrada_array = np.array([[ 
        entrada.budget,
        entrada.revenue,
        entrada.vote_count,
        entrada.popularity,
        entrada.Action,
        entrada.Adventure,
        entrada.Fantasy,
        entrada.Science,
        entrada.Fiction,
        entrada.Crime,
        entrada.Drama,
        entrada.Thriller,
        entrada.Animation,
        entrada.Family,
        entrada.Western,
        entrada.Comedy,
        entrada.Romance,
        entrada.Horror,
        entrada.Mystery,
        entrada.History,
        entrada.War,
        entrada.Music,
        entrada.Documentary,
        entrada.Foreign
    ]])
    
    
    entrada_escalada = X_scaler.transform(entrada_array)
    
    
    predicao_escalada = modelo_carregado.predict(entrada_escalada)
    
    
    predicao_original = y_scaler.inverse_transform(predicao_escalada)
    
    
    return {"predicao": float(predicao_original[0][0])}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)