from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

#Lê o csv
df = pd.read_csv(r'C:\Relatorio_cadop.csv', delimiter=';', encoding='utf-8') 
df = df.fillna('')  # substitui NaN por string vazia

#Cria rota get
@app.get("/operadoras")
def buscar_operadoras(busca: str = Query("")):
    
    termo = busca.lower()
    if 'Razao_Social' not in df.columns:
        return {"erro": "Coluna 'Razão Social' não encontrada no CSV"}
    
    resultado = df[df['Razao_Social'].str.lower().str.contains(termo)]
    return resultado.to_dict(orient='records')

#Rodar o servidor: python -m uvicorn ta:app --reload 
#Link do endpoind: http://localhost:8000/operadoras?busca