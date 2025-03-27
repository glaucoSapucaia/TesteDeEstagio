from .base import DataProcessorInterface
import pandas as pd

class DataProcessor(DataProcessorInterface):
    def __init__(self, abbreviation_dict: dict):
        self.abbreviation_dict = abbreviation_dict

    def process_data(self, tables):
        table_df = pd.concat(tables, ignore_index=True)
        table_df = table_df.rename(columns=self.abbreviation_dict)
        return table_df
