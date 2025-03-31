
# Projeto de Banco de Dados - Operadoras de Saúde

Este projeto tem como objetivo fornecer uma estrutura para o gerenciamento de dados de operadoras de plano de saúde, utilizando PostgreSQL e Docker para orquestrar o banco de dados. Através de arquivos SQL, são criadas as tabelas e carregados os dados de operadoras de planos de saúde, além de consultas para análise financeira.

## Estrutura do Projeto

A estrutura do projeto inclui:

- **Dockerfile**: Arquivo para configurar o ambiente PostgreSQL.
- **schema.sql**: Script para criar tabelas no banco de dados e importar dados.
- **queries.sql**: Consultas SQL para obter informações sobre as operadoras de planos de saúde.
- **data/**: Pasta contendo os arquivos CSV com os dados das operadoras de saúde e demonstrações contábeis.
- **diagram/**: Pasta contendo diagrama ERD.
- **util/normalizator.py**: Normaliza dados monetários da tabela.
- **README.md**: Este arquivo.

## Como usar

### Pré-requisitos

- Docker instalado no seu sistema.
- Acesso à internet para baixar a imagem do Docker.

### 1. Configuração do Banco de Dados com Docker

Para configurar o banco de dados PostgreSQL e inicializá-lo com os dados e schema fornecidos, siga as etapas abaixo:

1. **Clone o repositório**:

   ```bash
   git clone <url-do-repositorio>
   cd <diretorio-do-repositorio>
   ```

2. **Crie e inicie o container Docker**:

   Mude a porta ou garanta que não esteja sendo usada:

   ```bash
   sudo systemctl stop postgresql
   ```

   Execute o comando para construir e rodar o container Docker com a configuração do PostgreSQL:

   ```bash
   sudo docker build -t postgres_db .
   sudo docker run -d -p 5432:5432 --name ans_db postgres_db
   ```

   O Docker irá configurar o banco de dados PostgreSQL e rodar o serviço.

### 2. Carregar o Schema e os Dados

Os arquivos de dados em CSV serão carregados automaticamente para as tabelas no banco de dados através do `schema.sql`. Não é necessário executar nada manualmente, pois o Docker fará isso ao iniciar o container.

### 3. Realizar Consultas

Acesse o postgresql do container no modo iterativo:

```bash
sudo docker exec -it ans_db psql -U postgres
```

Acesse o banco de dados

```bash
\c ans_db
```

Depois de acessar o banco de dados, você pode executar as consultas SQL fornecidas no arquivo `queries.sql`. Por exemplo, para descobrir as 10 operadoras com maiores despesas no último trimestre, execute a consulta SQL no PostgreSQL:

```sql
SELECT COALESCE(o.nome_fantasia, o.razao_social) as operadora, o.cnpj,
    SUM(d.vl_saldo_final / 1000) AS total_despesa
FROM demonstracoes_contabeis_tb d
JOIN operadoras_de_plano_de_saude_ativas_tb o
    ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data_demonstracao BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY COALESCE(o.nome_fantasia, o.razao_social), o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;
```

As consultas no arquivo `queries.sql` incluem:

- **Consulta 1**: As 10 operadoras com maiores despesas no último trimestre.
- **Consulta 2**: As 10 operadoras com maiores despesas no último ano.

Na categoria: EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR

### 4. Saúde do Banco de Dados

Você pode verificar se o banco de dados está funcionando corretamente com o seguinte comando Docker:

```bash
sudo docker ps
```

O container deve estar em execução, e o PostgreSQL deverá estar aceitando conexões na porta 5432.

### Exemplo de Resultados

Aqui estão exemplos de respostas para as consultas SQL:

#### Consulta 1: Operadoras com maiores despesas no último trimestre

```sql
               operadora               |      cnpj      | total_despesa  
---------------------------------------+----------------+----------------
 BRADESCO SAUDE S.A.                   | 92693118000160 | $30,941,701.60
 SUL AMERICA COMPANHIA DE SEGURO SAÚDE | 01685053000156 | $21,124,940.41
 AMIL                                  | 29309127000179 | $20,820,818.06
...
```

#### Consulta 2: Operadoras com maiores despesas no último ano

```sql
               operadora               |      cnpj      |   total_despesa    
---------------------------------------+----------------+--------------------
 BRADESCO SAUDE S.A.                   | 92693118000160 | $77,467,609,279.79
 SUL AMERICA COMPANHIA DE SEGURO SAÚDE | 01685053000156 | $51,812,853,068.58
 AMIL                                  | 29309127000179 | $51,005,557,507.35
...
```

## Estrutura dos Arquivos

### Dockerfile

O arquivo `Dockerfile` configura o ambiente do PostgreSQL, incluindo a criação do banco de dados `ans_db`, e importa o schema e dados para as tabelas `operadoras_de_plano_de_saude_ativas_tb` e `demonstracoes_contabeis_tb`.

### schema.sql

Este arquivo contém o SQL para criar as tabelas e carregar os dados em formato CSV.

### queries.sql

Este arquivo contém as consultas SQL utilizadas para extrair informações do banco de dados.

## Contribuições

Se você quiser contribuir para o projeto, por favor, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.
