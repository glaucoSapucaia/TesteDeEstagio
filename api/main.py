from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from backend import CSVDataProvider

ROOT_DIR = Path(__file__).parent.resolve()
CSV_PATH = ROOT_DIR / 'backend' / 'data' / 'Relatorio_cadop.csv'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['GET'],
    allow_headers = ['*']
)

data_provider = CSVDataProvider(CSV_PATH)

@app.get('/buscar/')
def find_operator(q: str = Query(..., min_length=1)) -> list[dict]:
    results = data_provider.search_operators(q)
    return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8080)
