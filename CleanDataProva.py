import pandas as pd


def read_dataframe(file_name):
    df = pd.read_csv(file_name)

    return df.copy()
    