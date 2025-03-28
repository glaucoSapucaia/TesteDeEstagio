from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame

class CSVDataProviderInterface(ABC):
    @abstractmethod
    def _load_data(self) -> 'DataFrame':
        pass

    @abstractmethod
    def search_operators(self, query: str) -> list[dict]:
        pass
