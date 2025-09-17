import pandas as pd
from pathlib import Path
import pint
from pint.errors import UndefinedUnitError
import pint_pandas

class LookupTable:
    """
    A class to lookup values in a pandas DataFrame.
    Args:
        df: A pandas DataFrame.
        index_col: The column to use as the index of the DataFrame.
    """
    def __init__(self, df: pd.DataFrame, index_col: str):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df must be a pandas DataFrame")
        self.df = df.set_index(index_col)

    """
    Alternate constructor: build from a dictionary.
    """
    @classmethod
    def from_dict(cls, data: dict, index_col: str):
        return cls(pd.DataFrame(data), index_col)

    """
    Alternate constructor: build from a CSV file.
    Extra kwargs are passed to pd.read_csv (e.g., delimiter).
    """
    @classmethod
    def from_csv(cls, file_path: str | Path, index_col: str, **kwargs):
        raw_df = pd.read_csv(file_path, **kwargs)

        # Extract units from the column names (enclosed in square brackets)
        units = raw_df.columns.str.extract(r'\[(.*?)\]')

        assert len(units) == len(raw_df.columns), "Ensure that each column only specifies one [unit]"

        # Create a new DataFrame with PintArrays for the columns
        df_data = {}
        for i, col in enumerate(raw_df.columns):
            if i < len(units) and not pd.isna(units.iloc[i, 0]):
                # Column has units, create PintArray
                unit = units.iloc[i, 0]
                try:
                    df_data[col] = pd.Series(raw_df[col].values, dtype=f"pint[{unit}]")
                except UndefinedUnitError:
                    raise ValueError(f"Unit \"{unit}\" in table {file_path} is not a recognized unit")
            else:
                # Column has no units, keep as regular Series
                df_data[col] = raw_df[col]
        
        df = pd.DataFrame(raw_df)

        return cls(df, index_col)
    
    def get(self, key, field=None):
        row = self.df.loc[key]
        return row.to_dict() if field is None else row[field]

    def get_entries(self):
        return self.df.index.tolist()