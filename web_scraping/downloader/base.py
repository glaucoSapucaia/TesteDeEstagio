from abc import ABC, abstractmethod

class PDFDownloader(ABC):
    '''
    Interface para o downloader de PDFs.

    Esta classe abstrata define o método `download_pdfs` que deve ser implementado por qualquer classe 
    que herde de `PDFDownloader`. A implementação deve fornecer a lógica específica para o download 
    dos PDFs.
    '''
    @abstractmethod
    def download_pdfs(self) -> list:
        '''
        Método abstrato para download de PDFs.

        Este método deve ser implementado por subclasses para realizar o download dos PDFs.
        Ele deve retornar uma lista contendo os PDFs baixados.
        '''
        pass