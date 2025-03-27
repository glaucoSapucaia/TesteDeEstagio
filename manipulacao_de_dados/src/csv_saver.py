from .base import CSVSaverInterface
from typing import Any

class CsvSaver(CSVSaverInterface):
    def __init__(self, csv_path: Any):
        self.csv_path = csv_path

    def save_csv(self, data_frame: Any):
        data_frame.to_csv(str(self.csv_path), index=False, header=True)
