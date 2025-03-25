from .base import PDFDownloader
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests

class TestPDFDownloader(PDFDownloader):
    '''
    Concrete PDF Downloader
    '''
    def __init__(self, url: str, output_dir: Path):
        self.url = url
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True)
    
    def download_pdfs(self) -> list:
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception('Falha ao carregar a página!')
        
        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = [
            link['href']
            for link in soup.find_all('a', href=True)
            if link['href'].endswith('.pdf')
        ]

        pdf_files = []
        
        for href in pdf_links:
            pdf_url = urljoin(self.url, href)
            pdf_name = Path(urlparse(pdf_url).path).name

            if pdf_name.startswith(('Anexo_I', 'ANEXO_II')):
                pdf_path = self.output_dir / pdf_name
                self._download_pdf(pdf_url, pdf_path)
                pdf_files.append(pdf_path)
                print(f'PDF Downloaded - {pdf_name}.')
        
        return pdf_files

    @staticmethod
    def _download_pdf(url: str, path: Path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
