from typing import Any
import tabula
from .base import PDFExtractorInterface

class PdfExtractor(PDFExtractorInterface):
    def __init__(self, pdf_path: Any):
        self.pdf_path = pdf_path

    def extract_tables(self, pages: str):
        return tabula.read_pdf(str(self.pdf_path), pages=pages, multiple_tables=True, lattice=True)
