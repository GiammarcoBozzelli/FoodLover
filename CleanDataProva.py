import pandas as pd
import numpy as np


def read_dataframe(file_name):
    df = pd.read_csv(file_name)

    return df.copy()


def search_coordinate(df_data: pd.DataFrame, search_set: set) -> list:
    nda_values = df_data.values
    tuple_index = np.where(np.isin(nda_values, [e for e in search_set]))
    return [(row, col, nda_values[row][col]) for row, col in zip(tuple_index[0], tuple_index[1])]
