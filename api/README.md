# Projeto: Consulta de Operadoras Ativas - ANS

Este projeto fornece uma interface simples para consultar operadoras de saúde registradas na ANS (Agência Nacional de Saúde Suplementar). O backend é responsável por ler os dados de um arquivo CSV e expô-los via API, enquanto o frontend permite que o usuário busque informações de operadoras de saúde utilizando uma interface intuitiva.

## Estrutura do Projeto

```
.
├── backend/
│   └── data/
│   │   └── Relatorio_cadop.csv                  # Arquivo CSV contendo dados
│   ├── __init__.py
│   ├── base.py                                  # Inteface de CSVDataProvider
│   └── csv_data_provider.py                     # Código para leitura e manipulação dos dados CSV 
├── frontend/
│   └── index.html                               # Interface do usuário em HTML, com Vue.js e Bootstrap
├── postman
│   ├── postman_collection.json                  # Coleção Postman
│   ├── busca_operadora_send.jpeg                # Imagem de testes realizados
│   └── busca_operadora_testes.jpeg              # Imagem de testes realizados
├── main.py                                      # Script principal
└── README.md                                    # Este arquivo
```

## Tecnologias

### Backend:
- Python
- Pandas
- FastAPI (ou qualquer outro framework para criar a API)

### Frontend:
- HTML
- Vue.js
- Bootstrap
- Axios

### Ferramentas:
- Postman (para testar a API)
- Live Server

## Como Rodar o Projeto

### Backend

1. Instalar dependências: Certifique-se de ter o Python 3.x instalado e instale as dependências necessárias:

   ```bash
   pip install pandas fastapi uvicorn
   ```

2. Rodar a API:

   ```bash
   python3 main.py
   ```

   A API estará disponível em http://127.0.0.1:8080.

### Frontend

1. Abrir o `index.html`: Basta abrir o arquivo `frontend/index.html` no seu navegador para acessar a interface.
2. Interagir com a busca: Na interface, você pode digitar o nome da operadora para realizar a busca. A aplicação fará uma requisição à API backend e mostrará os resultados.

## Testes da API

Para testar as rotas da API, você pode importar o arquivo `postman/API Operadoras ANS.postman_collection.json` no Postman. Ele contém uma coleção de requisições que ajudam a testar a funcionalidade da API.

## Exemplo de Como Usar a API

### Endpoint de Busca

**GET** `/buscar/`

#### Parâmetros:
- `q`: (string) Termo para busca (ex: nome da operadora ou parte dele).

#### Exemplo de Requisição:

```bash
GET http://127.0.0.1:8000/buscar/?q=Unimed
```

A resposta será um JSON com a lista de operadoras que atendem ao critério de busca.

## Contribuição

Contribuições são bem-vindas! Para contribuir com o projeto, siga os seguintes passos:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Faça suas alterações e commite (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin minha-feature`).
5. Crie um Pull Request.
