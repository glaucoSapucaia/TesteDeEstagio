from compressor import ZipCompressor
from downloader import TestPDFDownloader
from pathlib import Path

if __name__ == '__main__':
    ROOT_DIR = Path(__file__).parent.resolve()
    PATH_DIR = ROOT_DIR / 'pdfs'
    url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

    downloader = TestPDFDownloader(url, PATH_DIR)
    downloaded_pdfs = downloader.download_pdfs()

    if downloaded_pdfs:
        ZipCompressor.compress(downloaded_pdfs, 'pdfs_files.zip', PATH_DIR)
        print('\nTudo certo! PDFs baixados e compactados...')