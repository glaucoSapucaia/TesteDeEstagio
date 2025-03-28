from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).parent.resolve()
CSV_PATH = ROOT_DIR / 'data' / 'Relatorio_cadop.csv'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['GET'],
    allow_headers = ['*']
)

df = pd.read_csv(CSV_PATH, delimiter=';')
df = df.fillna('N/A')

@app.get('/buscar/')
def find_operator(q: str = Query(..., min_length=1)):
    results = df[df['Nome_Fantasia'].str.contains(q, case=False, na=False)]
    return results.to_dict(orient='records')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8080)