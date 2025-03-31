-- Criação da tabela de operadoras de planos de saúde ativas
CREATE TABLE operadoras_de_plano_de_saude_ativas_tb (
    registro_ans INTEGER PRIMARY KEY,
    cnpj CHAR(14),
    razao_social VARCHAR(254),
    nome_fantasia VARCHAR(70),
    modalidade VARCHAR(50),
    logradouro VARCHAR(70),
    numero VARCHAR(30),
    complemento VARCHAR(50),
    bairro VARCHAR(30),
    cidade VARCHAR(30),
    uf CHAR(2),
    cep VARCHAR(8),
    ddd CHAR(2),
    telefone VARCHAR(30),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(100),
    representante VARCHAR(50),
    cargo_representante VARCHAR(50),
    regiao_de_comercializacao SMALLINT,
    data_registro_ans DATE
);

-- Criação da tabela de demonstrações contábeis
CREATE TABLE demonstracoes_contabeis_tb (
    data_demonstracao DATE,
    reg_ans INTEGER,
    cd_conta_contabil BIGINT,
    descricao VARCHAR(254),
    vl_saldo_inicial MONEY,
    vl_saldo_final MONEY
);

-- Criação de índices para otimizar as consultas
CREATE INDEX idx_operadoras ON operadoras_de_plano_de_saude_ativas_tb(registro_ans);
CREATE INDEX idx_demonstracoes ON demonstracoes_contabeis_tb(reg_ans);

-- Importação de dados da tabela de operadoras de planos de saúde ativas
COPY operadoras_de_plano_de_saude_ativas_tb (
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
    logradouro, numero, complemento, bairro, cidade, uf, cep,
    ddd, telefone, fax, endereco_eletronico, representante,
    cargo_representante, regiao_de_comercializacao,
    data_registro_ans
)
FROM '/docker-entrypoint-initdb.d/data/Relatorio_cadop.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');

-- Importação de dados das demonstrações contábeis por trimestre
-- Esta etapa pode ser automatizada com um script bash
COPY demonstracoes_contabeis_tb (
    data_demonstracao, reg_ans, cd_conta_contabil,
    descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/docker-entrypoint-initdb.d/data/ANS_demonstracao_contabil/2024/normalized1T2024.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis_tb (
    data_demonstracao, reg_ans, cd_conta_contabil,
    descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/docker-entrypoint-initdb.d/data/ANS_demonstracao_contabil/2024/normalized2T2024.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis_tb (
    data_demonstracao, reg_ans, cd_conta_contabil,
    descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/docker-entrypoint-initdb.d/data/ANS_demonstracao_contabil/2024/normalized3T2024.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis_tb (
    data_demonstracao, reg_ans, cd_conta_contabil,
    descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/docker-entrypoint-initdb.d/data/ANS_demonstracao_contabil/2024/normalized4T2024.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
