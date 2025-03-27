from pathlib import Path
from src import TableExtractor

if __name__ == '__main__':
    ROOT_DIR = Path(__file__).parent.resolve()
    CSV_DIR = ROOT_DIR / 'csv'
    CSV_DIR.mkdir(exist_ok=True)

    PDF_PATH = ROOT_DIR / 'pdf' / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    CSV_PATH = CSV_DIR / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv'
    CSV_ZIP_NAME = CSV_DIR / 'Teste_glauco_sapucaia.zip'

    abbreviations_dict = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }

    extractor = TableExtractor(PDF_PATH, CSV_PATH, CSV_ZIP_NAME, abbreviations_dict)
    extractor.run()
