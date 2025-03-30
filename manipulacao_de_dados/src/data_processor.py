from .base import DataProcessorInterface
import pandas as pd

class DataProcessor(DataProcessorInterface):
    def __init__(self, abbreviation_dict: dict):
        self.abbreviation_dict = abbreviation_dict

    def process_data(self, tables):
        # Verificando as tabelas extraídas
        print(f"Tabelas extraídas: {len(tables)}")
        print(f"0 - tabela extraída:\n{tables[0]}")
        print(f"50 - tabela extraída:\n{tables[50]}")
        print(f"100 - tabela extraída:\n{tables[100]}")
        print(f"150 -  tabela extraída:\n{tables[150]}")
        print(f"178 -  tabela extraída:\n{tables[178]}")

        if not tables:
            return pd.DataFrame()

        try:
            final_df = pd.concat(tables, axis=0)
        except Exception as e:
            print(f"ERRO na concatenação: {e}")
            return pd.DataFrame()

        # Renomeando as colunas de acordo com o dicionário
        final_df = final_df.rename(columns=self.abbreviation_dict)

        print("\nTabela final após processamento:")
        print(final_df.tail())

        colunas_lista = final_df.columns.tolist()
        print(colunas_lista)

        return final_df