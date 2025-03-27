from .base import ZipCompressorInterface
from typing import Any
import zipfile

class ZipCompressor(ZipCompressorInterface):
    def __init__(self, zip_path: Any):
        self.zip_path = zip_path

    def compress(self, file_path: Any):
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, file_path.name)
