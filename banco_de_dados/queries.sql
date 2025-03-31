-- 1. Quais as 10 operadoras com maiores despesas em 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' no último trimestre?

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

-- Resposta

--                operadora               |      cnpj      | total_despesa  
-- ---------------------------------------+----------------+----------------
--  BRADESCO SAUDE S.A.                   | 92693118000160 | $30,941,701.60
--  SUL AMERICA COMPANHIA DE SEGURO SAÚDE | 01685053000156 | $21,124,940.41
--  AMIL                                  | 29309127000179 | $20,820,818.06
--  NOTRE DAME INTERMÉDICA SAÚDE S.A.     | 44649812000138 |  $9,307,980.43
--  HAPVIDA                               | 63554067000198 |  $7,755,562.71
--  CASSI                                 | 33719485000127 |  $7,459,367.99
--  UNIMED NACIONAL                       | 02812468000106 |  $7,002,487.86
--  PREVENT SENIOR                        | 00461479000163 |  $5,920,615.05
--  UNIMED BH                             | 16513178000176 |  $5,411,476.03
--  SEGUROS UNIMED                        | 04487255000181 |  $4,824,024.16

-- 2. Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR " no último ano?

SELECT COALESCE(o.nome_fantasia, o.razao_social) as operadora, o.cnpj,
    SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis_tb d
JOIN operadoras_de_plano_de_saude_ativas_tb o
    ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data_demonstracao BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY COALESCE(o.nome_fantasia, o.razao_social), o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;

-- Resposta

--                operadora               |      cnpj      |   total_despesa    
-- ---------------------------------------+----------------+--------------------
--  BRADESCO SAUDE S.A.                   | 92693118000160 | $77,467,609,279.79
--  SUL AMERICA COMPANHIA DE SEGURO SAÚDE | 01685053000156 | $51,812,853,068.58
--  AMIL                                  | 29309127000179 | $51,005,557,507.35
--  NOTRE DAME INTERMÉDICA SAÚDE S.A.     | 44649812000138 | $23,545,735,832.81
--  HAPVIDA                               | 63554067000198 | $19,385,534,464.99
--  CASSI                                 | 33719485000127 | $18,412,177,093.19
--  UNIMED NACIONAL                       | 02812468000106 | $17,391,267,369.70
--  PREVENT SENIOR                        | 00461479000163 | $14,635,643,010.58
--  UNIMED BH                             | 16513178000176 | $13,162,050,667.89
--  SEGUROS UNIMED                        | 04487255000181 | $11,738,001,188.48
