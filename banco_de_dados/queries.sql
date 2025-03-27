-- 1. Quais as 10 operadoras com maiores despesas em 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' no último trimestre?

SELECT o.nome_fantasia, o.cnpj,
    SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis_tb d
JOIN operadoras_de_plano_de_saude_ativas_tb o
    ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data_demonstracao BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY o.nome_fantasia, o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;

-- Resposta

--     nome_fantasia    |      cnpj      |     total_despesa     
-- ---------------------+----------------+-----------------------
--  BRADESCO SAUDE S.A. | 92693118000160 | $3,089,592,678,705.00
--                      | 01685053000156 | $2,112,494,044,230.00
--  AMIL                | 29309127000179 | $1,384,524,317,274.00
--                      | 44649812000138 |   $922,747,167,356.00
--  HAPVIDA             | 63554067000198 |   $774,180,090,436.00
--  CASSI               | 33719485000127 |   $745,348,442,966.00
--  UNIMED NACIONAL     | 02812468000106 |   $673,748,997,121.00
--  PREVENT SENIOR      | 00461479000163 |   $592,061,507,862.00
--  UNIMED BH           | 16513178000176 |   $541,147,606,542.00
--  PORTO SEGURO SAÚDE  | 04540010000170 |   $463,597,168,606.00

-- 2. Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR " no último ano?

SELECT o.nome_fantasia, o.cnpj,
    SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis_tb d
JOIN operadoras_de_plano_de_saude_ativas_tb o
    ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data_demonstracao BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY o.nome_fantasia, o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;

-- Resposta

--     nome_fantasia    |      cnpj      |     total_despesa     
-- ---------------------+----------------+-----------------------
--  BRADESCO SAUDE S.A. | 92693118000160 | $7,741,706,935,544.00
--                      | 01685053000156 | $5,165,061,286,056.00
--  AMIL                | 29309127000179 | $4,292,023,882,206.00
--  HAPVIDA             | 63554067000198 | $1,910,691,055,906.00
--  CASSI               | 33719485000127 | $1,834,986,826,403.00
--  UNIMED NACIONAL     | 02812468000106 | $1,701,855,051,730.00
--                      | 44649812000138 | $1,661,091,861,782.00
--  PREVENT SENIOR      | 00461479000163 | $1,463,564,301,058.00
--  UNIMED BH           | 16513178000176 | $1,235,249,979,552.00
--  SEGUROS UNIMED      | 04487255000181 | $1,113,500,635,727.00
