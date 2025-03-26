from abc import ABC, abstractmethod

class PDFDownloader(ABC):
    '''
    PDF Downloader Interface
    '''
    @abstractmethod
    def download_pdfs(self) -> list:
        pass