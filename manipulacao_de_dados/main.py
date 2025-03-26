from pathlib import Path
import pandas as pd
import tabula
import zipfile

ROOT_DIR = Path(__file__).parent.resolve()
CSV_DIR = ROOT_DIR / 'csv'
CSV_DIR.mkdir(exist_ok=True)

PDF_PATH = ROOT_DIR / 'pdf' / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
CSV_PATH = CSV_DIR / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv'
CSV_ZIP_NAME = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.zip'

meu_nome = 'glauco_sapucaia'

abbreviations_dict = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}

tables = tabula.read_pdf(str(PDF_PATH), pages='3-181', multiple_tables=True)

if tables:
    print(f'Tabela extraida com sucesso - Total de linhas: {len(tables[0])}.')

    table_df = pd.concat(tables, ignore_index=True)

    table_df.to_csv(str(CSV_PATH), index=False, header=True)
    print(f'Arquivo CSV criado - {CSV_PATH}.')

    new_table_df = table_df.rename(columns=abbreviations_dict)

    with zipfile.ZipFile(CSV_DIR / f'Teste_{meu_nome}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(CSV_PATH, CSV_PATH.name)

    print(f'Tabela salva e compactada em {CSV_DIR / f'Teste_{meu_nome}.zip'}')

else:
    print(f'Nenhuma tabela encontrada.')

print(new_table_df.iloc[:, :5])