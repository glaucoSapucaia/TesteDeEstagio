from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from backend import CSVDataProvider

# Define o diretório raiz do projeto
ROOT_DIR = Path(__file__).parent.resolve()

# Caminho para o arquivo CSV que contém os dados
CSV_PATH = ROOT_DIR / 'backend' / 'data' / 'Relatorio_cadop.csv'

# Cria uma instância do FastAPI, que será o servidor da API
app = FastAPI()

# Adiciona middleware CORS para permitir que a API seja acessada de outros domínios
# Este procedimento foi devido a utilização da ferramenta Live Server
# Por se tratar de um teste, permite todos os dominios
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['GET'],
    allow_headers = ['*']
)

# Instancia o CSVDataProvider com o caminho do arquivo CSV
data_provider = CSVDataProvider(CSV_PATH)

# Rota GET para buscar operadoras
@app.get('/buscar/')
def find_operator(q: str = Query(..., min_length=1)) -> list[dict]:
    results = data_provider.search_operators(q)
    return results

# Inicia o servidor Uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8080)
