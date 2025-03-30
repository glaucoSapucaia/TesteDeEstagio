from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Importação para tipagem
if TYPE_CHECKING:
    from pandas import DataFrame

class CSVDataProviderInterface(ABC):
    """
    Interface abstrata para provedores de dados CSV.

    Define a estrutura básica para classes que irão carregar e buscar informações em arquivos CSV.
    """
    @abstractmethod
    def _load_data(self) -> 'DataFrame':
        """
        Método abstrato para carregar dados do CSV.

        Retorna:
            DataFrame: Um DataFrame do pandas contendo os dados carregados.
        """
        pass

    @abstractmethod
    def search_operators(self, query: str) -> list[dict]:
        """
        Método abstrato para buscar operadoras de saúde no dataset.

        Parâmetros:
            query: Termo de pesquisa para localizar operadoras.

        Retorna:
            list[dict]: Lista de dicionários contendo os dados das operadoras correspondentes.
        """
        pass
