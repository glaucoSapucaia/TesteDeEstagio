from .base import TableExtractorInterface
from .pdf_extractor import PdfExtractor
from .data_processor import DataProcessor
from .csv_saver import CsvSaver
from .zip_compressor import ZipCompressor
from typing import Any

class TableExtractor(TableExtractorInterface):
    def __init__(self, pdf_path: Any, csv_path: Any, zip_path: Any, abbreviation_dict: dict):
        self.pdf_path = pdf_path
        self.csv_path = csv_path
        self.zip_path = zip_path
        self.abbreviation_dict = abbreviation_dict

        self.pdf_extractor = PdfExtractor(pdf_path)
        self.data_processor = DataProcessor(abbreviation_dict)
        self.csv_saver = CsvSaver(csv_path)
        self.zip_compressor = ZipCompressor(zip_path)

    def run(self):
        tables = self.pdf_extractor.extract_tables(pages='3-181')
        if not tables:
            print("Nenhuma tabela encontrada.")
            return

        print(f'Tabela extraída com sucesso - Total de linhas da página um: {len(tables[0])}.')

        table_df = self.data_processor.process_data(tables)

        self.csv_saver.save_csv(table_df)
        print(f'Arquivo CSV criado - {self.csv_path}')

        self.zip_compressor.compress(self.csv_path)
        print(f'Tabela salva e compactada em {self.zip_path}')

        print(table_df.iloc[:, :5])
