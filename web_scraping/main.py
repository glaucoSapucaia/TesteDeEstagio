from compressor import ZipCompressor
from downloader import TestPDFDownloader
from pathlib import Path

# Bloco principal do script, executado quando o arquivo é chamado diretamente.
if __name__ == '__main__':
    # Define o diretório raiz (diretório onde o script está localizado)
    ROOT_DIR = Path(__file__).parent.resolve()

    # Define o diretório onde os PDFs baixados serão armazenados
    PATH_DIR = ROOT_DIR / 'pdfs'

    # URL da página web que contém os PDFs a serem baixados
    url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

    # Instancia o downloader de PDFs com a URL fornecida e o diretório de destino
    downloader = TestPDFDownloader(url, PATH_DIR)

    # Realiza o download dos PDFs da URL fornecida
    downloaded_pdfs = downloader.download_pdfs()

    # Se PDFs foram baixados com sucesso, compacta-os em um arquivo ZIP
    if downloaded_pdfs:
        ZipCompressor.compress(downloaded_pdfs, 'pdfs_files.zip', PATH_DIR)
        print('\nTudo certo! PDFs baixados e compactados...')
