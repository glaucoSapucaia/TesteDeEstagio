from .base import CSVDataProviderInterface
from typing import TYPE_CHECKING
import pandas as pd

if TYPE_CHECKING:
    from pathlib import Path
    from pandas import DataFrame

class CSVDataProvider(CSVDataProviderInterface):
    def __init__(self, csv_path: 'Path'):
        self.csv_path = csv_path
        self.df = self._load_data()

    def _load_data(self) -> 'DataFrame':
        df = pd.read_csv(self.csv_path, delimiter=';')
        return df.fillna('N/A')
    
    def search_operators(self, query: str) -> list[dict]:
        results = self.df[self.df['Nome_Fantasia'].str.contains(query,  case=False, na=False)]
        return results.to_dict(orient='records')
