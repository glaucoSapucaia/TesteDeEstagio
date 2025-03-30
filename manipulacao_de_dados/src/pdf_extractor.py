from typing import TYPE_CHECKING
import tabula
from .base import PDFExtractorInterface

# Importação para tipagem
if TYPE_CHECKING:
    from pandas import DataFrame
    from pathlib import Path

class PdfExtractor(PDFExtractorInterface):
    '''
    Implementação concreta da interface PDFExtractorInterface.

    Esta classe utiliza a biblioteca `tabula` para extrair tabelas de arquivos PDF.
    '''
    def __init__(self, pdf_path: 'Path') -> None:
        '''
        Inicializa o extrator de tabelas a partir de um arquivo PDF.

        Parâmetros:
        pdf_path: O caminho do arquivo PDF que será processado.
        '''
        self.pdf_path = pdf_path

    def extract_tables(self, pages: str) -> list['DataFrame']:
        '''
        Extrai tabelas de um arquivo PDF.

        O método utiliza a biblioteca `tabula` para ler tabelas presentes nas páginas especificadas do PDF.

        Parâmetros:
        pages: Identificação das páginas a serem processadas (exemplo: 'all', '1', '1-3', etc.).
        '''
        
        return tabula.read_pdf(str(self.pdf_path), pages=pages, multiple_tables=True, lattice=True)
