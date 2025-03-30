from pathlib import Path
from src import TableExtractor

# Inicialização do script
if __name__ == '__main__':
    # Define o diretório raiz do projeto
    ROOT_DIR = Path(__file__).parent.resolve()

    # Define e cria o diretório onde os arquivos CSV serão armazenados
    CSV_DIR = ROOT_DIR / 'csv'
    CSV_DIR.mkdir(exist_ok=True)

    # Caminho do arquivo PDF que será processado
    PDF_PATH = ROOT_DIR / 'pdf' / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

    # Caminho onde o arquivo CSV extraído será salvo
    CSV_PATH = CSV_DIR / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv'

    # Nome do arquivo ZIP onde o CSV será compactado
    CSV_ZIP_NAME = CSV_DIR / 'Teste_glauco_sapucaia.zip'

    # Dicionário de abreviações para renomear colunas do CSV
    abbreviations_dict = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }

    # Instancia o extrator de tabelas e executa o processo
    extractor = TableExtractor(PDF_PATH, CSV_PATH, CSV_ZIP_NAME, abbreviations_dict)
    extractor.run()
