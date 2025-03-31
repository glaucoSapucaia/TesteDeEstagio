import pandas as pd
import os

# Caminho da pasta onde os arquivos estão
FOLDER = '../data/ANS_demonstracao_contabil/2024'

# Listar todos os arquivos na pasta
files = [f for f in os.listdir(FOLDER) if f.endswith('.csv')]

# Iterar sobre os arquivos CSV
for file in files:
    file_path = os.path.join(FOLDER, file)

    # Ler o arquivo CSV
    df = pd.read_csv(file_path, delimiter=';')

    # Substituir a vírgula por ponto nas últimas duas colunas
    df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].apply(lambda x: str(x).replace(',', '.'))
    df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].apply(lambda x: str(x).replace(',', '.'))

    # Gerar o novo caminho do arquivo
    new_file = os.path.join(FOLDER, f"normalized{file}")
    
    # Salvar o arquivo alterado
    df.to_csv(new_file, index=False, sep=';')

    # debug
    print(f"Arquivo {file} processado e salvo como {new_file}")