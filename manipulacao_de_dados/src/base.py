from abc import ABC, abstractmethod
from typing import Any

class PDFExtractorInterface(ABC):
    '''
    PDF Extractor Interface
    '''
    @abstractmethod
    def extract_tables(self, pages: str):
        pass

class DataProcessorInterface(ABC):
    '''
    Data Processor Interface
    '''
    @abstractmethod
    def process_data(self, tables):
        pass

class CSVSaverInterface(ABC):
    '''
    CSV Saver Interface
    '''
    @abstractmethod
    def save_csv(self, data_frame: Any):
        pass

class ZipCompressorInterface(ABC):
    '''
    Zip Compressor Interface
    '''
    @abstractmethod
    def compress(self, file_path: Any):
        pass

class TableExtractorInterface(ABC):
    '''
    Table Extractor Interface
    '''
    @abstractmethod
    def run(self):
        pass
