from .base import PDFDownloader
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests

class TestPDFDownloader(PDFDownloader):
    '''
    Implementação concreta do downloader de PDFs.

    Esta classe herda de `PDFDownloader` e implementa o método `download_pdfs` para realizar o 
    download dos arquivos PDF a partir de uma página web específica. A classe também possui um 
    método auxiliar `_download_pdf` para baixar os PDFs.
    '''
    def __init__(self, url: str, output_dir: Path) -> None:
        '''
        Inicializa o downloader de PDFs com a URL da página e o diretório de saída.

        Parâmetros:
        url (str): URL da página web de onde os PDFs serão baixados.
        output_dir (Path): Diretório onde os PDFs baixados serão salvos.
        '''
        self.url = url
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True)
    
    def download_pdfs(self) -> list:
        '''
        Realiza o download dos PDFs encontrados na página web fornecida.

        Este método faz uma requisição HTTP para a URL especificada, analisa o conteúdo HTML da página 
        e encontra links para arquivos PDF. Em seguida, faz o download dos PDFs que atendem aos critérios 
        definidos (nome começando com 'Anexo_I' ou 'ANEXO_II') e os salva no diretório de saída.
        '''
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

                # debug
                print(f'PDF Downloaded - {pdf_name}.')
        
        return pdf_files

    @staticmethod
    def _download_pdf(url: str, path: Path) -> None:
        '''
        Baixa um arquivo PDF a partir de uma URL e o salva no caminho especificado.

        Parâmetros:
        url (str): URL do PDF a ser baixado.
        path (Path): Caminho onde o arquivo PDF será salvo.
        '''
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
