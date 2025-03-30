from .base import CSVDataProviderInterface
from typing import TYPE_CHECKING
import pandas as pd

# Importação para tipagem
if TYPE_CHECKING:
    from pathlib import Path
    from pandas import DataFrame

class CSVDataProvider(CSVDataProviderInterface):
    """
    Classe concreta para fornecer dados a partir de um arquivo CSV.

    Implementa a interface CSVDataProviderInterface, garantindo a leitura e consulta de operadoras de saúde.
    """
    def __init__(self, csv_path: 'Path') -> None:
        """
        Inicializa o provedor de dados CSV.

        Parâmetros:
            csv_path: Caminho do arquivo CSV contendo os dados das operadoras.
        """
        self.csv_path = csv_path
        self.df = self._load_data()

    def _load_data(self) -> 'DataFrame':
        """
        Carrega os dados do arquivo CSV para um DataFrame do pandas.

        Retorna:
            DataFrame: DataFrame contendo os dados carregados do CSV, com valores nulos substituídos por 'N/A'.
        """
        df = pd.read_csv(self.csv_path, delimiter=';')
        return df.fillna('N/A')
    
    def search_operators(self, query: str) -> list[dict]:
        """
        Pesquisa operadoras de saúde no dataset com base em um termo de consulta.

        Parâmetros:
            query: Termo de pesquisa para localizar operadoras.

        Retorna:
            list[dict]: Lista de dicionários contendo os dados das operadoras correspondentes.
        """
        results = self.df[self.df['Nome_Fantasia'].str.contains(query,  case=False, na=False)]
        return results.to_dict(orient='records')
